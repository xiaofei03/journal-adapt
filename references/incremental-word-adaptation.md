# Incremental Word Adaptation

## Word-Only Contract

- Count Zotero item and bibliography fields before every mutation.
- Copy the canonical journal manuscript into the active `_work/<run_id>/`; maintain one Chinese and one English work copy.
- Patch only identified paragraphs or objects. Never assign whole citation-bearing paragraphs through `paragraph.text`.
- Audit touched objects after each logical batch; run full-document gates once before delivery.
- If field counts decline, stop and restore the active work copy from the canonical journal manuscript.

## Cache Keys

Cache target profiles using journal slug, official-guide retrieval date, and source hash. Cache corpus style cards using PDF/Markdown SHA-256. Reuse a cache only when all keys match. Manuscript changes do not invalidate an unchanged journal profile.

## Durable Audit Set

Keep one issue map, one revision ledger, one final machine-readable audit, one concise human audit, and at most one contact sheet per language. Per-round Word copies and per-page renders are transient class-D artifacts.
