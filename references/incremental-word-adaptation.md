# Incremental Word Adaptation

## Word-Only Contract

- Count Zotero item and bibliography fields before every mutation.
- Copy the canonical journal manuscript into the active `_work/<run_id>/`; maintain one Chinese and one English work copy.
- Patch only identified paragraphs or objects. Never assign whole citation-bearing paragraphs through `paragraph.text`.
- Audit touched objects after each logical batch. Run full-document gates only for explicit submission delivery, not for a micro edit.
- If field counts decline, stop and restore the active work copy from the canonical journal manuscript.

## Micro Citation Repair

For a stale citekey, stale Zotero item URI, or a few missing bibliography sources:

1. Record citation-field and bibliography-field counts in the affected canonical files.
2. Patch only the target field ranges in temporary copies.
3. Refresh through Zotero/Word only when required.
4. Verify target current item URI or citekey present, stale identifier absent, field counts valid, one live bibliography retained, and no field-external citekey.
5. Replace the affected canonical manuscripts and stop.

Do not render the manuscript, hash every image, rebuild the submission package, or run unrelated formula/table/figure gates unless the patch actually changed those assets or the user requested submission delivery. If an Office refresh rewrites unrelated media, reject that saved file and report the escalation instead of silently launching a full merge-and-delivery cycle.

## Cache Keys

Cache target profiles using journal slug, official-guide retrieval date, and source hash. Cache corpus style cards using PDF/Markdown SHA-256. Reuse a cache only when all keys match. Manuscript changes do not invalidate an unchanged journal profile.

## Durable Audit Set

Keep one issue map, one revision ledger, one final machine-readable audit, one concise human audit, and at most one contact sheet per language. Per-round Word copies and per-page renders are transient class-D artifacts.
