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
7. Use `chinese-word-pro` for touched-feature QA, then run one full submission audit.
8. Replace canonical journal manuscripts only after Zotero, bilingual, figure, formula, table, and root-cleanliness gates pass.

Read `references/incremental-word-adaptation.md` for Word-only handling and cache invalidation.

## Preservation Priorities

1. Live Zotero fields and bibliography fields.
2. Numerical results, equations, table values, variable names, figure data, and hypothesis labels.
3. Frozen-mother provenance and cross-journal isolation.
4. Bilingual substantive equivalence.
5. Target-journal rhetoric and formatting.

## Final Outputs

Keep only the canonical manuscript pair, target profile, issue map, revision ledger, final audit, final figures, and submission package. Git records intermediate history.
