import os
import json
import time
from typing import List, Dict, Any
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv
from .prompts import CLASSIFICATION_PROMPT, TOPIC_CATEGORIES

# Load environment variables
load_dotenv()


class TopicClassification(BaseModel):
    """Pydantic model for topic classification response."""
    categorias: List[str]
    confianca: int
    palavras_chave: List[str]


def classify_political_chunks(chunks: List[Dict[str, Any]], 
                            model: str = "gemini-2.5-flash") -> List[Dict[str, Any]]:
    """
    Classify political manifesto chunks into policy topics using Gemini LLM with structured output.
    
    Args:
        chunks: List of chunk dictionaries from chunking.py
        model: Gemini model to use for classification
        
    Returns:
        List of chunks with added topic classification
    """
    # Configure Gemini API
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    classified_chunks = []

    print(f"Classifying {len(chunks)} chunks...")
    
    for i, chunk in enumerate(chunks):
        try:
            # Prepare content
            content = chunk["content"]
            
            # Add context from metadata if available
            context_info = []
            if chunk.get("metadata"):
                for key, value in chunk["metadata"].items():
                    if value and str(value).strip():
                        context_info.append(f"{key}: {value}")

            context = f"Contexto: {' | '.join(context_info)}\n\n" if context_info else ""
            full_content = f"{context}TEXTO:\n{content}"

            # Create the prompt with instructions
            prompt = f"{CLASSIFICATION_PROMPT}\n\n{full_content}"

            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": TopicClassification,
                }
            )

            # Parse structured response
            try:
                # Use the parsed response from Pydantic
                classification_obj: TopicClassification = response.parsed
                
                # Convert to dict
                classification = {
                    "categorias": classification_obj.categorias,
                    "confianca": classification_obj.confianca,
                    "palavras_chave": classification_obj.palavras_chave
                }
                
                # Validate categories against our topic list
                valid_categories = [cat for cat in classification["categorias"] if cat in TOPIC_CATEGORIES]
                if not valid_categories:
                    valid_categories = ["outros"]
                
                classification["categorias"] = valid_categories
                
                # Ensure confianca is in valid range
                classification["confianca"] = max(1, min(5, classification["confianca"]))
                
            except Exception as parse_error:
                print(f"Failed to parse structured response for chunk {i}: {parse_error}")
                # Fallback to raw text parsing
                try:
                    classification = json.loads(response.text)
                    if not isinstance(classification.get("categorias"), list):
                        classification["categorias"] = ["outros"]
                    classification.setdefault("confianca", 3)
                    classification.setdefault("palavras_chave", [])
                except:
                    classification = {
                        "categorias": ["outros"],
                        "confianca": 1,
                        "palavras_chave": [],
                        "error": str(parse_error)
                    }

            # Add classification to chunk
            enhanced_chunk = chunk.copy()
            enhanced_chunk["topics"] = classification["categorias"]  # For database
            enhanced_chunk["topic_classification"] = classification
            enhanced_chunk["classification_timestamp"] = time.time()

            classified_chunks.append(enhanced_chunk)
            
            if (i + 1) % 10 == 0:
                print(f"Processed {i + 1}/{len(chunks)} chunks")

        except Exception as e:
            print(f"Error classifying chunk {i}: {str(e)}")
            # Add chunk with error classification
            enhanced_chunk = chunk.copy()
            enhanced_chunk["topics"] = ["outros"]
            enhanced_chunk["topic_classification"] = {
                "categorias": ["outros"],
                "confianca": 1,
                "palavras_chave": [],
                "error": str(e)
            }
            classified_chunks.append(enhanced_chunk)

        # Small delay to avoid rate limiting
        time.sleep(0.2)

    print(f"Classification completed! {len(classified_chunks)} chunks processed.")
    return classified_chunks


def save_classified_chunks(classified_chunks: List[Dict[str, Any]], 
                          party_name: str, 
                          output_path: str) -> str:
    """
    Save classified chunks to JSON file.
    
    Args:
        classified_chunks: List of classified chunks
        party_name: Name of the party
        output_path: Path to save the file
        
    Returns:
        Path to saved file
    """
    # Generate summary
    topic_counts = {}
    for chunk in classified_chunks:
        topics = chunk.get("topics", [])
        for topic in topics:
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
    
    # Prepare output data
    output_data = {
        "party": party_name,
        "total_chunks": len(classified_chunks),
        "topic_distribution": dict(sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)),
        "processing_timestamp": time.time(),
        "chunks": classified_chunks
    }
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(classified_chunks)} classified chunks to {output_path}")
    print(f"Topic distribution: {topic_counts}")
    
    return output_path

