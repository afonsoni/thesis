"""
Text processing utilities for markdown content and party information extraction.
"""
import os
import re

def get_markdown_content(file_path):
    """Read and return raw markdown content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def get_party_info(file_name):
    """Extract party information from filename and return party metadata"""
    party_map = {
        'ad-2024': {'name': 'Aliança Democrática', 'affiliation': 'right'},
        'be-2024': {'name': 'Bloco de Esquerda', 'affiliation': 'left'},
        'chega-2024': {'name': 'CHEGA', 'affiliation': 'right'},
        'il-2024': {'name': 'Iniciativa Liberal', 'affiliation': 'right'},
        'livre-2024': {'name': 'LIVRE', 'affiliation': 'left'},
        'pan-2024': {'name': 'Pessoas-Animais-Natureza', 'affiliation': 'left'},
        'pcp-2024': {'name': 'Partido Comunista Português', 'affiliation': 'left'},
        'ps-2024': {'name': 'Partido Socialista', 'affiliation': 'left'}
    }
    
    for key, info in party_map.items():
        if key in file_name.lower():
            return info
    
    return {'name': 'Unknown', 'affiliation': 'unknown'}

def split_markdown_by_headers(content, file_name):
    """Split markdown content into chunks based on headers and add metadata"""
    from src.embeddings.topic_classifier import classify_topic
    
    chunks = []
    header_pattern = re.compile(r'^(#{1,6})\s+(.*)', re.MULTILINE)
    code_block_pattern = re.compile(r'^\s*```')
    
    # Get party information
    party_info = get_party_info(file_name)
    
    lines = content.split('\n')
    current_chunk = {'metadata': {}, 'content': ''}
    current_headers = {}
    prev_header_level = 0
    in_code_block = False
    
    # Configuration options
    include_headers_in_content = True
    filter_headers = ["Table of Contents", "This Page", "Navigation", "Índice"]
    
    for line in lines:
        # Track code blocks to avoid processing headers inside them
        if code_block_pattern.match(line):
            in_code_block = not in_code_block
        
        if not in_code_block:
            match = header_pattern.match(line)
            if match:
                # If there is content in the current chunk, process it
                if current_chunk['content'].strip():
                    current_chunk['content'] = current_chunk['content'].strip()
                    
                    # Add party metadata
                    current_chunk['metadata']['party_name'] = party_info['name']
                    current_chunk['metadata']['affiliation'] = party_info['affiliation']
                    current_chunk['metadata']['file_name'] = file_name
                    
                    # Classify topic
                    current_chunk['metadata']['topic'] = classify_topic(current_chunk['content'])
                    
                    chunks.append(current_chunk)
                    current_chunk = {'metadata': {}, 'content': ''}
                
                # Extract header information
                header_level = len(match.group(1))
                header_text = match.group(2).strip()
                
                # Clean header text
                header_text = re.sub(r'\\', '', header_text)
                header_text = re.sub(r'\[¶\]\(.*?\)', '', header_text).strip()
                header_text = re.sub(r'<[^>]+>', '', header_text)  # Remove HTML tags
                header_text = re.sub(r'\*\*', '', header_text)  # Remove markdown bold
                
                # Update current headers hierarchy
                if header_level <= prev_header_level:
                    # Remove headers of same or lower level
                    keys_to_remove = [k for k in current_headers.keys() 
                                    if int(k.split()[1]) >= header_level]
                    for k in keys_to_remove:
                        del current_headers[k]
                
                header_key = f'Header {header_level}'
                current_headers[header_key] = header_text
                
                # Set metadata for new chunk
                current_chunk['metadata'] = current_headers.copy()
                
                # Optionally include header in content
                if include_headers_in_content:
                    current_chunk['content'] += f"{match.group(1)} {header_text}\n"
                
                prev_header_level = header_level
            else:
                current_chunk['content'] += line + '\n'
        else:
            current_chunk['content'] += line + '\n'
    
    # Add the last chunk if it has content
    if current_chunk['content'].strip():
        current_chunk['content'] = current_chunk['content'].strip()
        current_chunk['metadata']['party_name'] = party_info['name']
        current_chunk['metadata']['affiliation'] = party_info['affiliation']
        current_chunk['metadata']['file_name'] = file_name
        current_chunk['metadata']['topic'] = classify_topic(current_chunk['content'])
        chunks.append(current_chunk)
    
    # Filter out unwanted chunks
    filtered_chunks = []
    for chunk in chunks:
        metadata = chunk['metadata']
        # Check if any header contains filtered terms
        should_filter = False
        for header_value in metadata.values():
            if isinstance(header_value, str) and any(term.lower() in header_value.lower() 
                                                   for term in filter_headers):
                should_filter = True
                break
        
        if not should_filter and len(chunk['content'].strip()) > 50:  # Minimum content length
            filtered_chunks.append(chunk)
    
    return filtered_chunks
