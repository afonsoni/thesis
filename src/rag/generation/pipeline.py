"""
Generation pipeline – thin wrapper that connects retrieval output to synthesis.
"""

import logging
from typing import Callable, Optional
from src.rag.common.models import PARTY_MAP, GeneratedAnswer, RetrievalResult
from src.rag.generation.prompts import OUT_OF_CORPUS_ANSWER
from src.rag.generation.synthesizer import synthesize

logger = logging.getLogger(__name__)


def generate(retrieval_result: RetrievalResult,
             on_token: Optional[Callable[[str], None]] = None) -> GeneratedAnswer:
    """
    Receive ranked chunks from retrieval and produce a ``GeneratedAnswer``.

    This is the single entry-point for the generation stage. *on_token*, if
    given, receives the answer text as it is generated (streaming).
    """
    if retrieval_result.closed_book:
        return synthesize(retrieval_result, on_token)
    query = retrieval_result.query
    if query.unlisted_parties and not query.parties:
        return GeneratedAnswer(
            answer=OUT_OF_CORPUS_ANSWER.format(
                parties=", ".join(query.unlisted_parties),
                corpus=", ".join(info["name"] for info in PARTY_MAP.values()),
            ),
            sources=[],
        )
    # ``any``: a fan-out where every party came back empty is still a dict of
    # (empty) lists, and would otherwise send the LLM a prompt with no context.
    if not retrieval_result.results and not any(retrieval_result.results_by_party.values()):
        return GeneratedAnswer(
            answer="Não foram encontrados documentos relevantes para responder a esta pergunta.",
            sources=[],
        )

    return synthesize(retrieval_result, on_token)
