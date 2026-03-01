"""
Topic classification module for political content using LLM or keyword-based approaches.
"""
import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

# Define available topics
POLITICAL_TOPICS = [
    "Taxes (impostos)",
    "Social Security (segurança social)", 
    "Work (trabalho)",
    "Housing (habitação)",
    "Health (saúde)",
    "Education (educação)",
    "Safety (segurança)",
    "Justice (justiça)",
    "Foreign affairs (política externa)",
    "Culture (cultura)",
    "Environment (ambiente)",
    "Other (outros)"
]

# Topic keywords for fallback classification
TOPIC_KEYWORDS = {
    'Taxes': ['imposto', 'tributação', 'fiscal', 'taxa', 'irs', 'iva', 'irc'],
    'Social Security': ['segurança social', 'pensões', 'reforma', 'subsídio', 'prestação social'],
    'Work': ['trabalho', 'emprego', 'laboral', 'trabalhador', 'empregador', 'sindicat', 'salário'],
    'Housing': ['habitação', 'casa', 'arrendamento', 'imobiliário', 'habitacional'],
    'Health': ['saúde', 'hospital', 'médico', 'sns', 'cuidados de saúde', 'medicina'],
    'Education': ['educação', 'escola', 'ensino', 'professor', 'estudante', 'universidade'],
    'Safety': ['segurança', 'crime', 'polícia', 'proteção civil', 'bombeiros'],
    'Justice': ['justiça', 'tribunal', 'juiz', 'direito', 'lei', 'jurídico'],
    'Foreign affairs': ['política externa', 'diplomacia', 'internacional', 'europa', 'nato'],
    'Culture': ['cultura', 'arte', 'património', 'museu', 'teatro', 'cinema'],
    'Environment': ['ambiente', 'clima', 'ecologia', 'sustentabilidade', 'verde', 'carbono', 'energia'],
    'Other': []  # Default category
}

def classify_topic_with_llm(content, use_gemini=True, model_name="gemini-2.0-flash-exp"):
    """Classify the topic of a content chunk using an LLM"""
    
    # Create the prompt for classification
    prompt = f"""You are a political content classifier. Analyze the following text from a Portuguese political program and classify it into ONE of the following topics:

{chr(10).join([f"- {topic}" for topic in POLITICAL_TOPICS])}

Text to classify:
{content[:1000]}...

Instructions:
- Return ONLY the topic name in English (e.g., "Taxes", "Health", "Education", etc.)
- If the text doesn't clearly fit any specific topic, return "Other"
- Be precise and choose the most relevant topic

Topic:"""

    try:
        if use_gemini:
            # Use Google Gemini API
            model = genai.GenerativeModel(model_name)
            
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.1,
                    max_output_tokens=20,
                    top_p=0.8,
                    top_k=40
                )
            )
            
            if response.text:
                classification = response.text.strip()
                
                # Extract just the topic name (remove any extra text)
                for topic in ["Taxes", "Social Security", "Work", "Housing", "Health", 
                             "Education", "Safety", "Justice", "Foreign affairs", "Culture", 
                             "Environment", "Other"]:
                    if topic.lower() in classification.lower():
                        return topic
                
                return "Other"
            else:
                print("Gemini API returned empty response")
                return classify_topic_fallback(content)
                
        else:
            # Use Ollama local API as fallback
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1,
                        "num_predict": 20
                    }
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                classification = result.get("response", "Other").strip()
                
                # Extract just the topic name (remove any extra text)
                for topic in ["Taxes", "Social Security", "Work", "Housing", "Health", 
                             "Education", "Safety", "Justice", "Foreign affairs", "Culture", 
                             "Environment", "Other"]:
                    if topic.lower() in classification.lower():
                        return topic
                
                return "Other"
            else:
                print(f"Ollama API error: {response.status_code}")
                return classify_topic_fallback(content)
            
    except Exception as e:
        print(f"LLM classification error: {e}")
        return classify_topic_fallback(content)

def classify_topic_fallback(content):
    """Fallback keyword-based classification if LLM fails"""
    content_lower = content.lower()
    
    # Count matches for each topic
    topic_scores = {}
    for topic, keywords in TOPIC_KEYWORDS.items():
        if topic == 'Other':
            continue
        score = sum(1 for keyword in keywords if keyword in content_lower)
        if score > 0:
            topic_scores[topic] = score
    
    # Return the topic with highest score, or 'Other' if no matches
    if topic_scores:
        return max(topic_scores, key=topic_scores.get)
    else:
        return 'Other'

def classify_topic(content):
    """Main topic classification function - uses LLM with fallback to keywords"""
    return classify_topic_with_llm(content)
