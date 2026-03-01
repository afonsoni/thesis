"""
Generation pipeline – thin wrapper that connects retrieval output to synthesis.
"""

import logging
from src.rag.common.models import GeneratedAnswer, RetrievalResult
from src.rag.generation.synthesizer import synthesize

logger = logging.getLogger(__name__)


def generate(retrieval_result: RetrievalResult) -> GeneratedAnswer:
    """
    Receive ranked chunks from retrieval and produce a ``GeneratedAnswer``.

    This is the single entry-point for the generation stage.
    """
    if not retrieval_result.results and not retrieval_result.results_by_party:
        return GeneratedAnswer(
            answer="Não foram encontrados documentos relevantes para responder a esta pergunta.",
            sources=[],
            query_type=retrieval_result.query.query_type,
        )

    return synthesize(retrieval_result)
