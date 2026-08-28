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

## Fast WPS Open and Zotero Refresh

Use this route whenever a Word-only journal manuscript must be opened in WPS for Zotero refresh or final inspection.

### Open the exact work copy directly

1. Resolve and verify the absolute path of the active `_work/<run_id>/` DOCX before opening it.
2. Prefer the current Codex file preview's application `Open` action when the file is already displayed; it hands the exact artifact directly to WPS.
3. If that action is unavailable to automation, launch the verified path directly with the operating system, for example `open -a 'WPS Office' '<absolute-docx-path>'` on macOS.
4. If WPS already has several tabs open, activate the tab whose window title exactly matches the target filename; `ctrl+Tab` may be used to cycle tabs while checking the title after each step.

Do not open the WPS home-page or custom file-selection dialog and then browse or type the path. Do not close, save, or alter unrelated open documents while locating the target tab.

### Refresh quickly and deterministically

1. Confirm Zotero is running and the target WPS window title matches the verified work copy.
2. Open the WPS `Zotero` ribbon and invoke `Refresh` once. Prefer an accessibility-index click. If the ribbon control is not exposed through accessibility, use a fresh screenshot and a coordinate click on the visible `Refresh` control; never reuse coordinates from an earlier UI state.
3. Wait for the refresh operation to finish, handle only dialogs that clearly belong to the target document, and save the same work copy with the normal save command.
4. Run a field-aware audit before promotion. At minimum verify unchanged-or-expected item-field count, exactly one live bibliography field, balanced field markers, parseable citation JSON, expected unique cited-item count, matching bibliography-entry count, no missing or uncited entries, and no citekeys outside fields.
5. Promote the refreshed work copy to the canonical journal manuscript only after those checks pass.

A script may automate direct opening, waiting, saving, or audit steps when it can verify the exact target path and active window. It must not bypass the live Zotero/WPS refresh merely by rewriting visible citation text or bibliography XML. If refresh reduces fields, creates parse errors, leaves the bibliography stale, or rewrites unrelated protected content, reject the refreshed copy and restore from the last healthy work copy.

## Cache Keys

Cache target profiles using journal slug, official-guide retrieval date, and source hash. Cache corpus style cards using PDF/Markdown SHA-256. Reuse a cache only when all keys match. Manuscript changes do not invalidate an unchanged journal profile.

## Durable Audit Set

Keep one issue map, one revision ledger, one final machine-readable audit, one concise human audit, and at most one contact sheet per language. Per-round Word copies and per-page renders are transient class-D artifacts.
