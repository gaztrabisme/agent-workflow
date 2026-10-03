# RAG / Retrieval Heuristics

These are the decision rules for retrieval systems: whether retrieval is needed, what to index and return, how to combine retrieval stages, and how to measure retrieval quality. Use `references/templates/eval-harness.md` before optimizing.

## Decide whether retrieval is needed

For literal identifiers and codebase lookups, prefer exact-match search when it is stronger, and use it alongside semantic retrieval. Keyword search catches exact and rare terms while dense retrieval captures broader meaning. [book:essential-graphrag], 3.1 Step-back prompting

Skip retrieval when the entire relevant corpus fits in the model's context window and direct context is adequate. Long context alone does not guarantee the model uses all of it well; for a static corpus, retrieve focused excerpts instead of assuming a larger window makes retrieval unnecessary. [book:ai-engineering-huyen], RAG

For single-hop lookup over structured material, start with hybrid retrieval. Add graph retrieval only when real queries require multi-hop reasoning. [book:art-of-ai-product-development], Engineering corner: GraphRAG Enhances RAG with structured knowledge

## Chunk for matching and context

Separate the small child match unit from the larger parent context unit. Index child chunks, link each to its parent, and deduplicate parents before returning context. Small sections can match precisely while the parent retains enough context to answer. [book:essential-graphrag], 3.2 Parent document retriever

Count chunk size with the tokenizer used by the downstream model, not a word-count estimate. Token-based chunking is tied to that tokenizer; changing models may require reindexing. [book:ai-engineering-huyen], Chunking strategy

Respect document structure: split on heading boundaries, preserve code blocks as atomic units when possible, token-bound oversized prose, and re-fence code when a hard split is unavoidable. Content-aware chunkers can preserve code fences so examples stay paired with explanations. [book:building-reliable-ai-systems], Finding the sweet spot: Content-aware chunking

Add small overlap within the same parent when a useful answer may cross chunk boundaries. Overlap preserves some boundary information; do not let it create unnecessary duplicate results. [book:ai-engineering-huyen], Chunking strategy

Prepend the heading path or equivalent section metadata to the embedded text. Embed the child match unit with its heading path, not the full parent context unit. [book:building-reliable-ai-systems], Summary; [book:essential-graphrag], 3.2 Parent document retriever

Keep remote and local embedding-input construction identical so local evaluation predicts the deployed representation.

## Build hybrid retrieval and reranking

Use dense retrieval for semantic matching and sparse BM25 for exact terms, rare identifiers, and acronyms. Combining term-based and embedding-based retrieval is hybrid search. [book:ai-engineering-huyen], Combining retrieval algorithms

Use a real BM25 implementation with suitable tokenization, stopwords, and IDF rather than a hand-built regular-expression/hash tokenizer. BM25 remains a strong lexical baseline. [book:ai-powered-search], 3.2.1 BM25: The industry standard default text-similarity algorithm

Prefer server-side distribution-based fusion of dense and sparse scores when the store supports it; otherwise measure the client-side fusion method on the target corpus.

A cross-encoder reranker is a strong quality lever after the faster retrieval stages, when it fits the candidate count and latency budget. Cross-encoders are more expensive per query but usually more accurate, so select the tier from measured candidate volume and service constraints. [book:ai-powered-search], 13.8 Cross-encoders vs. bi-encoders

When the caller is an LLM agent, expose query expansion as caller-supplied inputs and keep the sparse BM25 query original. Account for the expansion's token, latency, and monetary cost in the caller path; generating extra queries is not free.

Prefer a calibrated absolute reranker score floor with a minimum-results guard over a gap-based cutoff when score distributions make gaps unstable.

## Treat enrichment and advanced retrieval as experiments

Treat LLM-generated contextual enrichment as an experiment, not a default. Evaluate it by query-to-relevant-item ranking, not by the intrinsic quality of generated summaries. Gate it on the full index against a pre-registered no-enrichment baseline, and keep the system without enrichment if it loses.

If enrichment is used, write the added context in the searcher's likely problem or symptom language. [book:ai-engineering-huyen], Contextual retrieval. It can be especially risky on jargon-heavy and extractive corpora, where generated prose can blur the exact terms the search depends on.

Use late chunking only when the embedding model supports mean pooling and the target-corpus evaluation shows a win.

The basic multistage foundation—hybrid BM25 and dense retrieval followed by cross-encoder reranking—combines broad recall with better precision. Default to this without per-query LLM work; reserve more expensive query-time methods for query types that need them. [book:building-reliable-ai-systems], The role of each component

Use graph retrieval when actual queries require multi-hop reasoning, and compare embedding models and reranking choices on the target corpus rather than selecting by leaderboard rank. [book:art-of-ai-product-development], Engineering corner: GraphRAG Enhances RAG with structured knowledge

Add retrieval enhancements only after the hybrid-and-rerank foundation runs out of measured headroom and each addition beats the pre-registered baseline. Do not train a reinforcement-learning retriever by default; let the caller supply HyDE or multi-query variants when that is sufficient.

## Retrieval evaluation

Build a tool-agnostic retrieval harness before optimizing. [book:ai-engineering-huyen], Design Your Evaluation Pipeline. Score at the unit the consumer receives, commonly the returned parent, and choose ranking, recall, or first-hit metrics that serve the decision.

Use fusion-only Recall@50 as a diagnostic to distinguish retrieval misses from reranking misses. Keep a hard vocabulary-gap set as the gate and an easier chunk-vocabulary set as a regression guard.

Include diverse query archetypes and report each stratum. Include at least one expected-to-fail or unanswerable stratum so the evaluation measures false confidence as well as successful retrieval. Validate any LLM relevance judge against human labels on this corpus before using its scores. [book:ai-engineering-huyen], Why AI as a Judge?
