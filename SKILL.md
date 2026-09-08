---
name: journal-adapt
description: "Adapt a frozen academic submission mother to one locked target journal using verified journal profiles and corpus-derived writing signals, with Word-only incremental revision, bilingual equivalence, Zotero-field preservation, cached style analysis, isolated journal versions, submission packaging, and final audits. Use after journal-selection-pro has locked a destination."
---

# Journal Adapt

Adapt one frozen submission mother to one locked destination. This skill does not select journals and does not modify empirical facts.

## Entry Gate

Require:

- `submission_strategy/journal_decision.json` with `status: locked`.
- A frozen Chinese/English submission mother or an explicitly English-only mother.
- A verified journal profile with official-guide retrieval dates.
- A clean target slug not shared with another journal version.

Run `scripts/init_journal_version.py` once. It copies the mother into an isolated journal directory and records source hashes. Never edit or overwrite the mother.

## Canonical Journal Directory

```text
journal_versions/<slug>/
  profile/
  manuscript/cn/
  manuscript/en/
  figures/
  audits/
  submission/
  revision_ledger.md
  version_state.json
```

Temporary Word files, page renders, and probes belong in the active `_work/<run_id>/`, not in `audits/` or the project root.

## Adaptation Pipeline

1. Build or reuse the target profile. Cache corpus conversion and style cards by file hash.
2. Create one `audits/issue_map.md` containing priorities, evidence limits, and immutable objects.
3. Revise positioning, theory, and structure in one temporary Word pair.
4. Revise methods/results claim strength without changing equations, variables, samples, estimates, tables, or citations unless evidence explicitly supports the change.
5. Perform native-level English editing while maintaining content equivalence with the Chinese companion.
6. Append changes to one `revision_ledger.md`; do not create numbered round manuscripts.
7. Use `chinese-word-pro` for touched-feature QA. Run one full submission audit only when the user requests a submission-ready delivery or the task changes multiple protected surfaces.
8. Replace canonical journal manuscripts after the gates appropriate to the declared task class pass; full Zotero, bilingual, figure, formula, table, and root-cleanliness gates remain mandatory for submission delivery.

Read `references/incremental-word-adaptation.md` for Word-only handling and cache invalidation.

## Micro-Edit Fast Lane

When the target journal and canonical manuscript are already known and the request changes only a few known text runs, citation links, captions, cells, or one object:

- patch only the affected language files in one temporary work pair;
- when WPS/Zotero interaction is required, use the direct-open and single-refresh route in `references/incremental-word-adaptation.md`; do not browse through WPS's custom file-selection dialog;
- run only the matching pre/post gate;
- aim for five minutes for a prepared micro edit; after two failures change the approach and explain the concrete issue, continuing safe authorized work;
- rebuild affected submission derivatives only when synchronization/delivery is requested; otherwise mark dependent outputs stale, including appendix citations affected by renumbering;
- reuse journal profiles, corpus analysis and unchanged page renders; do not reopen completed stages without a changed dependency;
- do not rerun formula, figure, table, or root audits for citation-only or text-only work;
- stop after the narrow gate passes, replace the canonical file, update the revision ledger briefly, and commit.

If the narrow repair changes unrelated media, fields, pagination, or structures, stop and disclose the escalation trigger before expanding scope.

For final submission, read `references/submission-handoff.md` for file roles, page-count evidence and post-submission freezing.

## Preservation Priorities

1. Live Zotero fields and bibliography fields.
2. Numerical results, equations, table values, variable names, figure data, and hypothesis labels.
3. Frozen-mother provenance and cross-journal isolation.
4. Bilingual substantive equivalence.
5. Target-journal rhetoric and formatting.

## Final Outputs

Keep only the canonical manuscript pair, target profile, issue map, revision ledger, final audit, final figures, and submission package. Git records intermediate history.
