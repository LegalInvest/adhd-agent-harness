# ADHD × AI LLM-Wiki Schema

This local knowledge export follows the LLM-Wiki pattern:

- `raw/sources/`: immutable source snapshots produced by daily scout runs.
- `wiki/daily/`: daily scout digest pages.
- `wiki/evidence/`: one evidence card per reusable source.
- `wiki/topics/`: one seed page per content pack, generated separately.
- `index.md`: navigation entry point.
- `log.md`: chronological operation log.

The content engine is non-destructive. Evidence can recommend upgrades or
replacements, but actual content-pack replacement requires explicit human approval
and an archive entry under `archive/topic-replacements/`.
