"""
Evaluation stage for the RAG system.

A fourth pipeline stage (alongside indexing / retrieval / generation) that measures
implementation steps against each other and against a naive baseline:

- ``variants``  – the declarative ladder of implementation steps (RetrievalConfig presets).
- ``dataset``   – synthetic-anchored + curated gold set construction.
- ``metrics``   – retrieval, routing, and LLM-judge generation metrics.
- ``runner``    – run one variant over the dataset.
- ``report``    – aggregate + persist results and the comparison leaderboard.
- ``pipeline``  – ``evaluate(...)`` orchestrator (single entry point).
"""
