#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from openai import OpenAI
from embeddings.embeddings import search_embeddings

# Load environment variables from .env file
load_dotenv()

# Get API token from environment variables
api_token = os.getenv("LLAMA_API_TOKEN")
if not api_token:
    raise ValueError("LLAMA_API_TOKEN not found in environment variables")

def format_context(search_results):
    """Format search results into a context string for the LLM"""
    context_parts = []
    
    for i, hit in enumerate(search_results):
        context_parts.append(
            f"Document {i+1} (from {hit['entity']['file_name']}):\n{hit['entity']['content']}"
        )
    
    return "\n\n".join(context_parts)

def query_llm(query, context, system_prompt=None):
    """Query the LLaMA API with context and user query"""
    client = OpenAI(
        api_key=os.getenv("LLAMA_API_TOKEN"),
        base_url="https://api.apillm.com/"
    )
    
    # Default system prompt if none provided
    if system_prompt is None:
        system_prompt = """És um assistente prestável que responde a perguntas com base no contexto fornecido.
        Se a resposta não puder ser derivada do contexto, diz "Não tenho informação suficiente para responder a esta pergunta."
        Cita sempre qual o documento que usaste para responder à pergunta.
        Responde sempre em português europeu, de forma clara e concisa."""
    
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
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Erro ao consultar a API LLaMA: {str(e)}")

def rag_query(query, top_k=5, system_prompt=None):
    """Complete RAG pipeline: search embeddings and query LLM with context"""
    # Search for relevant documents
    search_results = search_embeddings(query, top_k)
    
    if not search_results or not search_results[0]:
        return "No relevant documents found to answer your question."
    
    print(f"Found {len(search_results)} relevant documents for the query: '{query}'")
    print(f"Using top {top_k} documents for context.")
    
    for i, hit in enumerate(search_results[0]):
        print(f"\nResult {i+1} (Similarity Score: {hit['distance']:.4f}):")
        print(f"From file: {hit['entity']['file_name']}")
        print(f"Content: {hit['entity']['content'][:200]}...")
    
    # Format search results as context
    context = format_context(search_results[0])
    
    # Query LLM with context
    query_llm(query, context, system_prompt)
