# FP P3 — Archive core and adapters

Owner: Gary. Branch: `unit/fp-P3`. Completed: 2026-10-15. Acceptance: passed. Contracts: proposed for Gary's approval. No commit, merge or push performed.

## Result

One core now serves Domestika, Coursera, book, paper and repository adapters. `bash scripts/fp/accept-archive.sh` passes **59 tests**, including all **33 existing tests**. The final run took 19.608 seconds. No real-site requests, browser automation, cookies, account credentials, new dependencies, model loading or GPU work were used. All repository edits stayed in this worktree; knowledge-base inputs were read-only.

The core owns reconciliation, shared permitted transports, content hashing, the sanitized manifest, portable reading documents, verification, immutable publication, ZIP packaging/privacy and pending handoff. Each adapter implements the seven approved operations. Existing `package_domestika.py` and `reading_copy.py` commands remain valid; their ZIP creation/insertion now delegates to the core. Successful legacy ZIP and English reading-copy builds automatically emit `<output-stem>.handoff/` sidecars through the same adapter/core; derived unit PDF prose is mapped to its original inputs, and English PDF chunks retain translation labels plus a referenced removal log. The mature HLS language/height/duration/protection selector remains in use.

## Key decisions and grounding

- Pattern: intrinsic-artifact gate. Acceptance compares explicit member sets, opens actual locator text/pixels, instruments transfer/normalization/PDF-open seams, kills real processes, corrupts handoffs and runs privacy rejection probes. Independent read-only review supplied additional adversarial reproductions.
- Grounding: approved `design-spec.md`, “Ingestion and the archive skill”, “Migration plan / Archive core and handoff”, proving cases and “Repo layout and distribution”; `product-brief.md`; P2 `CONTRACTS.md`, source identity, locator, catalog entry, evidence read and existing book registry. Existing P2 book IDs use `book:<slug>` with aliases; logical source IDs are caller-supplied/stable, never inferred from a mutable title.
- Shared identity and locator schemas are byte-identical copies of P2. Their SHA-256 values are `c28e9fc667254b142f25968aa696b474eb412415d8f4872954e479036c3cd87b` and `21c526ef87e6bf87bf051e3376f65b2d070e792e18a2fa7ba1e1616da801416a`, respectively. Final equality was checked against `unit/fp-P2`.
- Recovery: asset and normalization checkpoints are durable independently; staging never becomes a publication. `CURRENT` is the atomic visibility boundary. Scope history is saved after the pointer commits. Tests: `test_interruption_recovery_every_adapter_repeated_kills`, `test_pointer_write_failure_does_not_advance_scope_history`.
- Reconciliation: removal requires authoritative rediscovery of that same scope, and can remove only that scope's previously known members. Repeated narrower selection/lost access retains earlier evidence; tombstones retain bytes and prior releases. Tests: `test_failed_discovery_never_deletes_and_narrower_selection_preserves`, `test_authoritative_same_scope_removal_tombstones_retains_bytes`, `test_lost_access_keeps_prior_evidence`.
- Measurement: `new_transfers` counts completed non-inline transport operations; `new_parses` counts normalization operations. Unchanged runs additionally prove no PDF parser opens and no hidden re-normalization during production validation. A processing-profile change reparses while reusing verified transferred assets and preserving the original source identity/hash. Public `validate` intentionally performs an independent locator/pixel audit.
- Implementation process: the walking skeleton preceded the expanded test suite. Discriminating regressions and independent review subsequently verified the final implementation; no test-first claim is made for that initial skeleton.

## Adapter evidence

Exact ordered member sets, rerun counters, output paths and sample locators are recorded in [P3-evidence.json](P3-evidence.json). The acceptance script prints the retained artifact directory for coordinator inspection.

| Case | Expected = actual membership | Unchanged rerun | Distinguishing evidence |
|---|---|---|---|
| Domestika | `unit:1`, `lesson:11`, `unit:2`, `lesson:12` | 4 reused; 0 transfers/parses | Locked lesson counted; native Spanish and requested English cues; master audio/subtitle groups; stream audio/duration/height/protection checks. |
| Coursera progressive | `module:m1`, `activity:v1`, `activity:r1`, `activity:r2`, `activity:q1` | 5 reused; 0 transfers/parses | Direct MP4/VTT; typed reading text; widget unresolved; quiz locked; unknown total is null / not found. |
| Coursera locked | Same 5 listed IDs | 5 reused; 0 transfers/parses | All four activities remain locked, including the widget. |
| Book | `pdf`, `epub` | 2 reused; 0 transfers/parses | Real generated two-page PDF and two-resource EPUB; editions/metadata/headings; physical page geometry; zero-based spine order; scanned page OCR status; raster/vector and repeated EPUB image occurrences. |
| Paper | `abstract`, `pdf` | 2 reused; 0 transfers/parses | Logical `arxiv:2601.00001`, exact `arxiv:2601.00001v2`, preserved PDF text/page. Separate DOI abstract-only case stays partial. |
| Repository | `file:README.md`, `file:danger.py`, `file:src/helper.txt` | 3 reused; 0 transfers/parses | Fixed commit `e763a86a3686e6592e01eb46de349630270a00ec`; dirty working text ignored; no source execution; separate README-only selection. |

Every main adapter was killed at `after-transfer`, `after-parse` and `before-publish`, then resumed and rerun: **15 actual SIGKILL recovery exercises**. Durable completed transfer records remain identical across recovery. Before-publication kills resume with zero new transfers/parses. An injected failure between release rename and pointer update leaves the previous release active and does not advance removal authority. Both proving cases `failed_discovery_never_deletes` and `release_install_preserves_outbox` have nonempty fixtures and explicit assertions.

The fixture repository is deterministically created by the tests, and its commit is asserted against the fixed hash above. Its executable-looking source is only read as bytes. A malicious promisor Git configuration also proves that missing blobs cannot launch a repository-configured helper: lazy fetch, external transports, hooks, fsmonitor and replacement objects are disabled.

## Contracts for approval

All schemas are draft 2020-12, validate offline and reference the shared source identity/locator by their existing URNs. No shared shape was redefined.

| New schema in `contracts/v1/` | Purpose / v1 gap |
|---|---|
| `archive-manifest.json` | `archive-manifest/v1`: ordered/expected membership, access, assets, hashes, normalized evidence, figures, dates, scope, rights/privacy, independent archive/handoff states, gaps, counters and derivations. |
| `kb-handoff.json` | `kb-handoff/v1`: exact manifest/JSONL/blob descriptors, source, membership/counts and receipt-governed completion. |
| `archive-locator.json` | References shared locator; adds asset byte/HTML offsets, EPUB image occurrences and saved-frame requested/actual time with explicit not-found status. |
| `figure-occurrence.json` | Keeps occurrence identity, physical/resource/cue context, source and pixel assets, caption status and nearby spans separately from deduplicated pixel blobs. |
| `text-chunk.json` | Pure normalized-block handoff with parent/child IDs, original/translation/derived label, source/producing revisions, embedding-input hash, figure IDs and separate child/parent/context spans. |
| `image-record.json` | Pixel blob/hash plus exact occurrence and source/producing revision. |

Each of these six proposed contracts has committed positive and negative JSON fixtures in `tests/fixtures/contracts/`. The compatibility bridge has separate offline proofs of concurrent caller snapshot isolation and hash/policy-cached media verification, and a proof of unit PDF membership, duplicate-prose prevention, translation labels, referenced removal log and zero-transfer/parse rerun. The two copied P2 schemas are also checked for schema validity. New contracts await Gary/coordinator approval; no consumer or indexing contract implementation was added elsewhere.

## Privacy, handoff and review

Restricted `.state/` is mode 0700; `transport.json` is mode 0600. Supplied playback/download capabilities never enter released descriptors. The scanner rejects credential-like query/fragment parameters and nested encoded URLs in metadata, raw/rendered PDFs, HTML, handoffs, reports, ZIP members/comments/extra fields and nested archives. It handles long URLs across scan chunks, including four encoding depths. Large stored MP4s remain supported; excessive nested/decompression input fails closed. Rendering localizes ordinary raster images and disables remote renderer loading.

Handoff validation checks schema, exact role/path binding, source and member identity, active/tombstoned membership, blob/chunk/figure sets, byte counts/hashes, embedding inputs, span provenance and actual locator/pixel contents before any future model import. Generated reading PDFs are referenced blobs with mappings to their original normalized inputs, avoiding duplicate prose ingestion. Emission remains `pending`; no saved/indexed receipt is fabricated.

Independent review found and reproduced hidden rerun PDF parsing, repeated narrowed-scope deletion, corrupted installed releases, HTTP query identity collisions, mutable-title locator spoofing, Git lazy-fetch helper execution, source/privacy contamination, scope-history ordering, multilingual PDF glyph loss, wrong stream selection, large-video ZIP rejection and privacy scanner boundary/metadata omissions. All received corrections and regression coverage. Focused bridge review additionally caught caller-snapshot races, unverified preserved media, self-derived pixel inputs and missing removal logs; unique private inputs, hash/policy probe checkpoints, original-only derivation inputs and required referenced logs close those findings. The reviewer confirmed the final encoded-boundary reproduction rejects and reported **no open findings**. It edited no files.

## Final checks and scope limits

- `bash scripts/fp/accept-archive.sh`: 59/59 passed, including existing tests; artifact directory and examples in `P3-evidence.json`.
- All 8 schemas pass Draft 2020-12 meta-schema validation; all 12 new-contract positive/negative cases pass their intended result.
- Legacy command `--help` smoke checks, Python compilation, skill quick validation and `git diff --check` passed.
- First-page book, Domestika and progressive Coursera PDFs were rendered with Poppler and visually inspected: readable original text, explicit locked/unresolved/OCR gaps, no clipping or overlap. Multilingual extraction separately proves Chinese and Greek survive the portable PDF.
- Fixtures total **79,223 bytes**, well below 5 MB. PDFs, EPUB, captions and one-second media are synthetic and generated locally. No real signed URLs or private course text are committed.
- Installed packages used: PyMuPDF 1.27.2.2, jsonschema 4.23.0, Pillow 11.3.0; existing ffmpeg/ffprobe. EPUB uses standard-library ZIP/XML. No package installation occurred.

Acceptance proves recorded source-snapshot replay, not current live-site markup or fresh remote entitlement. Refresh discovery snapshots/content fingerprints when upstream assets change; unchanged replay is not a live freshness claim. OCR is reported rather than performed; caption matching for figures remains explicit/heuristic with missing captions marked, not invented. The generic portable PDF lays out original text; the preserved Domestika English translation/frame/audit workflow remains separate. Consumer indexing and shared installer integration remain later phases.

Coordinator rerun: `bash scripts/fp/accept-archive.sh` from this worktree outside the sandbox. Inspect the printed artifact root's `test_every_adapter_membership.../<case>/CURRENT`, corresponding `manifest.json`, JSONL records and referenced blobs; run `python3 scripts/archive.py validate <release>` to independently open locators. Review the six proposed contracts before merging. The coordinator owns committing.
