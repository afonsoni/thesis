from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from typing import List, Dict, Any

def chunk_political_manifesto(markdown_content: str, max_chunk_size: int = 1000, chunk_overlap: int = 100) -> List[Dict[str, Any]]:
    """
    Chunk political manifesto markdown content by headers with windowing for large chunks.
    
    Args:
        markdown_content: The markdown content to chunk
        max_chunk_size: Maximum size in characters for each chunk (default: 1000)
        chunk_overlap: Overlap size in characters between chunks (default: 100)
        
    Returns:
        List of dictionaries with chunk content, metadata, and size info
    """
    # Tailored for political documents
    headers_to_split_on = [
        ("#", "Title"),
        ("##", "Major_Section"),
        ("###", "Policy_Area"), 
        ("####", "Policy_Topic"),
        ("#####", "Subsection"),
        ("######", "Details"),
    ]
    
    # First split by headers
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )
    
    header_chunks = markdown_splitter.split_text(markdown_content)
    
    # Create recursive splitter for large chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", "! ", "? ", ", ", " ", ""]
    )
    
    # Process each header chunk
    meaningful_chunks = []
    chunk_id = 0
    
    for header_chunk in header_chunks:
        content = header_chunk.page_content.strip()
        
        # Skip very small chunks
        if len(content) <= 50:
            continue
            
        # If chunk is within size limit, keep as is
        if len(content) <= max_chunk_size:
            meaningful_chunks.append({
                'id': chunk_id,
                'content': content,
                'metadata': header_chunk.metadata,
                'size': len(content),
                'word_count': len(content.split()),
                'chunk_type': 'header_only'
            })
            chunk_id += 1
        else:
            # Split large chunks with windowing
            sub_chunks = text_splitter.split_text(content)
            
            for i, sub_chunk in enumerate(sub_chunks):
                # Create enhanced metadata for sub-chunks
                enhanced_metadata = header_chunk.metadata.copy()
                enhanced_metadata['sub_chunk_index'] = i
                enhanced_metadata['total_sub_chunks'] = len(sub_chunks)
                enhanced_metadata['parent_chunk_size'] = len(content)
                
                meaningful_chunks.append({
                    'id': chunk_id,
                    'content': sub_chunk,
                    'metadata': enhanced_metadata,
                    'size': len(sub_chunk),
                    'word_count': len(sub_chunk.split()),
                    'chunk_type': 'windowed'
                })
                chunk_id += 1
    
    return meaningful_chunks
