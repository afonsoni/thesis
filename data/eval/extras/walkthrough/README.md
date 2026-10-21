# Walkthrough transcripts (for Results § PoliRAG in practice)

Verbatim `python main.py query "…"` output, run 2026-10-22 on the frozen code
(`code-freeze`, `0293a0b`; no code has changed since). Nothing is edited. None
of these questions is in the gold set.

| File | Question | What happened |
|---|---|---|
| `01-single-party.txt` | O que propõe o LIVRE para a habitação? | One LIVRE-filtered search, 10 excerpts, an answer in the manifesto's own four blocks with `[n]` citations; 5 sources, $0.0008 |
| `02-comparison.txt` | Compara as propostas do BE e da IL para o Serviço Nacional de Saúde. | Per-party search for BE and IL, a section per party; 13 sources, $0.0010 |
| `03-topic.txt` | Que partidos falam sobre o bem-estar animal? | Fan-out over all 8 parties, a section per party; 34 sources, $0.0023 |
| `04-general.txt` | Que propostas existem para combater a corrupção? | All parties, 64 excerpts, one narrative answer grouped by kind of measure; 37 sources, $0.0023 |
| `05-refusal.txt` | O que propõe o PCP sobre criptomoedas? | PCP-filtered search, nothing relevant, the hedged refusal ("isso não garante que os programas não abordem o tema"); the PCP manifesto never mentions crypto |
| `06-followup-1.txt` | Quais são os planos da AD para a habitação? | A normal single-party answer |
| `07-followup-2.txt` | E o PS? | **The failure case.** Each call is stateless, so the follow-up loses "habitação": PoliRAG searches the PS manifesto with no topic and refuses |

Each transcript shows the pipeline steps with timings, the answer, the sources
with their scores, and the LLM calls with tokens and cost.
