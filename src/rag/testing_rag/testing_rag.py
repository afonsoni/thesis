#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
from embeddings.embeddings import search_embeddings, generate_and_store_embeddings

# Load environment variables from .env file
load_dotenv()

# Configure Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

def format_context(search_results):
    """Format search results into a context string for the LLM"""
    context_parts = []
    
    for i, hit in enumerate(search_results):
        entity = hit['entity']
        party_name = entity.get('party_name', 'Unknown')
        topic = entity.get('topic', 'Unknown')
        affiliation = entity.get('affiliation', 'unknown')
        
        # Build header context
        headers = []
        for j in range(1, 7):  # Check for headers 1-6
            header_key = f'header_{j}'
            if header_key in entity and entity[header_key]:
                headers.append(entity[header_key])
        
        header_context = " > ".join(headers) if headers else "No specific section"
        
        context_parts.append(
            f"Document {i+1} (Party: {party_name}, Topic: {topic}, Affiliation: {affiliation}, Section: {header_context}):\n{entity['content']}"
        )
    
    return "\n\n".join(context_parts)

def query_llm_with_gemini(query, context, system_prompt=None, model_name="gemini-2.0-flash-exp"):
    """Query Google Gemini with context and user query"""
    
    # Default system prompt if none provided
    if system_prompt is None:
        system_prompt = """És um assistente especializado em análise de programas políticos portugueses.
        Responde com base no contexto fornecido dos programas eleitorais.
        Se a resposta não puder ser derivada do contexto, diz "Não tenho informação suficiente para responder a esta pergunta."
        Cita sempre qual o partido/documento que usaste para responder à pergunta.
        Quando comparares diferentes partidos, menciona as suas posições políticas (esquerda/direita).
        Responde sempre em português europeu, de forma clara e estruturada."""
    
    try:
        # Initialize the model
        model = genai.GenerativeModel(model_name)
        
        # Combine system prompt, context and query
        full_prompt = f"{system_prompt}\n\nContexto:\n{context}\n\nPergunta: {query}\n\nResposta:"
        
        # Generate response
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.3,
                max_output_tokens=1000,
                top_p=0.8,
                top_k=40
            )
        )
        
        return response.text
        
    except Exception as e:
        return f"Erro ao consultar Gemini: {str(e)}"

def query_llm_with_api(query, context, system_prompt=None):
    """Query the LLaMA API with context and user query (fallback option)"""
    api_token = os.getenv("LLAMA_API_TOKEN")
    if not api_token:
        return "LLAMA_API_TOKEN not found in environment variables"
    
    client = OpenAI(
        api_key=api_token,
        base_url="https://api.apillm.com/"
    )
    
    # Default system prompt if none provided
    if system_prompt is None:
        system_prompt = """És um assistente especializado em análise de programas políticos portugueses.
        Responde com base no contexto fornecido dos programas eleitorais.
        Se a resposta não puder ser derivada do contexto, diz "Não tenho informação suficiente para responder a esta pergunta."
        Cita sempre qual o partido/documento que usaste para responder à pergunta.
        Quando comparares diferentes partidos, menciona as suas posições políticas (esquerda/direita).
        Responde sempre em português europeu, de forma clara e estruturada."""
    
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"Contexto:\n{context}\n\nPergunta: {query}"
        }
    ]
    
    try:
        response = client.chat.completions.create(
            messages=messages,
            model="llama3.3-70b",
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao consultar a API LLaMA: {str(e)}"

def enhanced_rag_query(query, top_k=5, system_prompt=None, filter_party=None, filter_topic=None, filter_affiliation=None, use_gemini=True, model_name="gemini-2.0-flash-exp"):
    """Enhanced RAG pipeline with LLM-classified topics and improved querying"""
    
    print(f"🔍 Searching for: '{query}'")
    if filter_party:
        print(f"📊 Filtered by party: {filter_party}")
    if filter_topic:
        print(f"🏷️ Filtered by topic: {filter_topic}")
    if filter_affiliation:
        print(f"⚖️ Filtered by affiliation: {filter_affiliation}")
    
    # Search for relevant documents with optional filters
    search_results = search_embeddings(query, top_k, filter_party, filter_topic, filter_affiliation)
    
    if not search_results or not search_results[0]:
        return "No relevant documents found to answer your question."
    
    print(f"\n✅ Found {len(search_results[0])} relevant documents")
    print(f"📄 Using top {top_k} documents for context\n")
    
    # Display search results with enhanced information
    for i, hit in enumerate(search_results[0]):
        entity = hit['entity']
        print(f"📋 Result {i+1} (Similarity Score: {hit['distance']:.4f}):")
        print(f"   🏛️ Party: {entity.get('party_name', 'Unknown')}")
        print(f"   🏷️ Topic: {entity.get('topic', 'Unknown')}")
        print(f"   ⚖️ Affiliation: {entity.get('affiliation', 'unknown')}")
        
        # Show header hierarchy
        headers = []
        for j in range(1, 7):
            header_key = f'header_{j}'
            if header_key in entity and entity[header_key]:
                headers.append(entity[header_key])
        
        if headers:
            print(f"   📑 Section: {' > '.join(headers)}")
        
        print(f"   📝 Content preview: {entity['content'][:150]}...")
        print()
    
    # Format search results as context
    context = format_context(search_results[0])
    
    # Query LLM with context (prefer Gemini for API processing)
    print("🤖 Generating response...\n")
    
    if use_gemini:
        response = query_llm_with_gemini(query, context, system_prompt, model_name)
    else:
        response = query_llm_with_api(query, context, system_prompt)
    
    print("💬 Response:")
    print("=" * 50)
    print(response)
    print("=" * 50)
    
    return response

def regenerate_embeddings_with_llm():
    """Regenerate all embeddings using the enhanced LLM-based topic classification"""
    print("🔄 Regenerating embeddings with LLM-based topic classification...")
    print("⚠️  This will recreate the entire collection with new topic classifications\n")
    
    try:
        generate_and_store_embeddings()
        print("\n✅ Successfully regenerated embeddings with LLM topic classification!")
    except Exception as e:
        print(f"\n❌ Error regenerating embeddings: {str(e)}")

def test_topic_classification():
    """Test the LLM topic classification on sample content"""
    from src.embeddings.topic_classifier import classify_topic_with_llm, classify_topic_fallback
    
    test_content = """
    O Governo compromete-se a reduzir a carga fiscal sobre as famílias e empresas.
    Propomos uma diminuição do IRS para os escalões mais baixos e uma simplificação
    do sistema tributário. As empresas beneficiarão de uma redução do IRC para
    promover o investimento e a criação de emprego.
    """
    
    print("🧪 Testing LLM topic classification:")
    print(f"Content: {test_content[:100]}...")
    
    # Test Gemini classification
    gemini_topic = classify_topic_with_llm(test_content, use_gemini=True)
    print(f"🤖 Gemini Classification: {gemini_topic}")
    
    # Test fallback classification
    fallback_topic = classify_topic_fallback(test_content)
    print(f"🔤 Fallback Classification: {fallback_topic}")

def compare_parties_on_topic(topic, affiliation_filter=None):
    """Compare different parties' positions on a specific topic"""
    print(f"📊 Comparing party positions on: {topic}")
    if affiliation_filter:
        print(f"⚖️ Filtered by affiliation: {affiliation_filter}")
    
    # Search for documents on this topic
    search_results = search_embeddings(
        query=topic,
        top_k=10,
        filter_topic=topic,
        filter_affiliation=affiliation_filter
    )
    
    if not search_results or not search_results[0]:
        print("❌ No documents found for this topic")
        return
    
    # Group results by party
    party_positions = {}
    for hit in search_results[0]:
        entity = hit['entity']
        party_name = entity.get('party_name', 'Unknown')
        affiliation = entity.get('affiliation', 'unknown')
        
        if party_name not in party_positions:
            party_positions[party_name] = {
                'affiliation': affiliation,
                'content_pieces': []
            }
        
        party_positions[party_name]['content_pieces'].append({
            'content': entity['content'][:300],
            'score': hit['distance']
        })
    
    # Display comparison
    print(f"\n🏛️ Found positions from {len(party_positions)} parties:\n")
    
    for party, data in party_positions.items():
        print(f"🔹 {party} ({data['affiliation']}):")
        for i, piece in enumerate(data['content_pieces'][:2]):  # Show top 2 pieces per party
            print(f"   📝 Position {i+1}: {piece['content']}...")
            print(f"   📊 Relevance Score: {piece['score']:.4f}")
        print()

if __name__ == "__main__":
    # Example usage and testing
    print("🚀 Enhanced RAG System with Gemini 2.0 Flash Topic Classification")
    print("=" * 60)
    
    # Test topic classification
    print("\n1. Testing Topic Classification:")
    test_topic_classification()
    
    # Example queries
    print("\n2. Example Enhanced RAG Queries:")
    
    # Query about taxes
    print("\n" + "="*30)
    enhanced_rag_query("Quais são as propostas sobre impostos?", top_k=3, filter_topic="Taxes")
    
    # Compare health policies between left and right
    print("\n" + "="*30)
    enhanced_rag_query("Como é que os partidos de direita abordam a saúde?", top_k=3, filter_affiliation="right", filter_topic="Health")
    
    # Topic comparison
    print("\n3. Topic Comparison:")
    compare_parties_on_topic("Education", affiliation_filter="left")