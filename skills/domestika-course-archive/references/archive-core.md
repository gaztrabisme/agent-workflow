# Shared archive core and five adapters

The existing Domestika ZIP command also emits `<zip-stem>.handoff/`, and the English reading-copy build emits `<pdf-stem>.handoff/`. Each sidecar uses this same core, preserves local verified unit PDFs/media/captions, and remains pending. Unit PDF prose reuses its normalized original inputs; English reading PDFs retain translation labels and a referenced removal log. These directories remain separate from the unchanged ZIP member layout.

The source repositories remain separate from pi-mind and the knowledge base. This repository owns archive behavior; the checked-in P2 source-identity and locator copies are unchanged shared contracts. There are no model imports, consumer writes or automatic indexing.

## Run, inspect and validate

```sh
python3 scripts/archive.py run tests/fixtures/archive/book.json --output /path/to/book-work
cat /path/to/book-work/CURRENT
python3 scripts/archive.py validate /path/to/book-work/releases/<generation>
python3 scripts/archive.py scan /path/to/book-work/releases/<generation>
python3 scripts/archive.py install-release /path/to/verified-release --output /path/to/book-work
bash scripts/fp/accept-archive.sh
```

`run` requires a local JSON source snapshot, with paths relative to that snapshot. A work directory belongs to one logical source/adapter/privacy scope. Use the existing source registry ID when available (`book:<slug>` for existing P2 books); do not infer identity from a mutable display title. Every successful invocation prints actual transfer/normalization counters and its immutable release path. `CURRENT` is the publication boundary. Source bytes, normalized evidence and prior releases remain available across tombstones.

Layout:

```text
<source-work>/
  CURRENT                         # atomic relative pointer to verified data
  releases/<generation>/
    manifest.json                 # sanitized archive-manifest/v1
    kb-handoff.json               # pending; no invented consumer receipt
    text-chunks.jsonl
    image-records.jsonl
    reading-copy.md
    reading-copy.pdf               # faithful original text in a derived layout
    blobs/<sha256>                 # referenced source/document/pixel bytes
  .state/                         # mode 0700; durable transfers/parses/staging
    transport.json                # mode 0600; excluded from every release
  outbox/                         # mutable local drafts, never replaced by install
```

Do not bundle the work directory. Distribute only a validated immutable release within the owner's authorized private channel. `install-release` validates the source and destination, refuses identity/privacy conflicts, changes only immutable releases and their pointer, and preserves local outbox and staging.

## Adapter operations and source snapshots

Every adapter implements `capabilities`, `discover`, `collect`, `probe`, `resolve_transport`, `normalize`, `source_checks`. The adapters translate structure, source facts and access states. The core owns reconciliation, transport execution, hash storage, privacy, document generation, packaging and handoff.

The committed snapshots in `tests/fixtures/archive/` are executable input examples:

| Adapter | Snapshot and preserved structure | Access and limits |
|---|---|---|
| Domestika | Existing collector JSON (`course_id`, `course_title`, expected units/lessons and ordered `units`); units and lessons become members. Native/requested VTT cues and HLS selection remain explicit. | Existing ZIP/reading-copy CLIs remain available. The streaming transport reuses their language/height/duration/DRM policies. Recorded `media_fixture`/`playlist_fixture` paths are only for offline proofs. Missing captions/protection fail transfer; listed locked members survive. |
| Coursera | `source_id`, ordered `modules` with typed `items` (`typeName`, `isLocked`, reading `content.html`, lecture `files` with direct `downloadUrl`, media type, role and optional SHA-256). | Uses ordinary direct HTTP files; no alternate playback access. Progressive inventory has `inventory_complete: false`. Embedded `ungradedWidget` readings remain unresolved; locked activities remain locked, including widgets. |
| Book | Stable `source_id`, `files` with member ID/local path, edition and optional language. | PDF physical pages, labels/geometry, metadata/headings and raster/vector occurrences are retained. EPUB metadata, headings, spine order, internal resources and repeated raster occurrences survive. Scanned pages are `ocr-required`; garbled text is `extraction-failure`, with original bytes retained. No OCR engine is invoked. |
| Paper | Exact `arxiv` identifier ending in `vN`, or `doi`; abstract plus accessible PDF/HTML `files`. | Logical arXiv identity and exact-version alias are separate; DOI remains explicit. Abstract-only is partial. No OpenAlex dependency. |
| Repository | `source_id`, local `repo`, exact `commit`, optional selected `files`. | Inventories the committed tree and reads only selected blobs as inert text. Working-tree edits are irrelevant. README-only remains README-only; symlinks/submodules remain unsupported members. Git hooks, fsmonitor, replacement objects, lazy fetch and external transports are disabled. |

Common snapshot fields include `title`, `canonical_url`, `creators`, `publication_date`, `revision_date`, `privacy_scope`, `scope`, `rights`, `inventory_complete`, `discovery_ok` and optional independently recorded `expected_membership`. Dates not discovered remain null with reason `not found`; incomplete expected totals/membership do too. Complete inventory counts include structural units/modules and all listed activities, including locked/unsupported ones. Exact membership compares stable IDs, not just totals.

Recorded snapshots are source-structure fixtures, not a claim that current live sites were recaptured. The Domestika HTML mirrors the collector's `article.paper`, lesson IDs and `__INITIAL_PROPS__`; the playlists mirror audio/subtitle groups. The acceptance script never drives a browser or contacts a real site. Direct HTTP is exercised against recorded byte responses; selected Git repositories are created locally at a deterministic commit.

## Privacy and rendering

The core strips transport URLs and machine paths from asset descriptors before hashing/distribution. It stores temporary capabilities only in a restricted projection; it never reads browser cookies or account tokens. Ordinary query parameters still distinguish different assets; changing only a temporary signing parameter does not invalidate content.

The release gate inspects nested metadata, HTML entities/percent encodings, JSON escapes, signed/token query and fragment parameters, rendered PDF text/links/metadata/streams, ZIP comments/extra fields and nested members. Large stored videos are scanned in chunks; unfinished URLs are carried across boundaries and overlong incomplete URLs fail closed. ZIP nesting/decompression limits defend the scanner without rejecting ordinary large MP4 members. Never weaken the gate to distribute a signed link.

Rendering localizes ordinary raster images before Chrome runs and refuses other remote-loading constructs. The generic core renders already normalized text with PyMuPDF Story and no external resources. Original source files remain separate from derived portable documents.

## Incremental reconciliation and recovery

Durable checkpoints exist independently for verified transferred assets and normalized parses. Content identities and processing fingerprints exclude signing parameters. Member metadata changes do not invalidate unchanged asset parsing; repository commit changes can update locators over unchanged blobs. Hashes are rechecked before reuse. Privacy scan checkpoints bind the exact hash and scanner profile. An unchanged rerun invokes neither transfer nor normalization nor PDF parsing; fresh JSON/schema/path/hash checks still run. The separate public `validate` command deliberately opens locators and regenerates occurrences as an independent audit.

Counters are disjoint member outcomes (`added`, `changed`, `reused`, `quarantined`, `removed`) plus `new_transfers` (completed non-inline transport operations) and `new_parses` (normalization operations). A completed checkpoint reused after a kill is `reused`, even if that interrupted attempt never published. Locked new members count as added; loss of access to an existing member quarantines it while retaining its evidence. A removal is counted only on its first tombstone transition.

Failed discovery never changes an existing publication into an empty inventory. Narrower selection never authorizes removal, including on repeated narrow runs. Scope history records authoritative inventories after the publication pointer commits. Only a new authoritative inventory of that same scope can tombstone its formerly known missing members. Tombstones preserve blobs and earlier release generations. Earlier evidence carries its producing source revision/commit in handoff provenance.

The core serializes runs with a file lock, writes and fsyncs checkpoints, validates staging, renames the complete release and then atomically updates `CURRENT`. Incomplete staging is never published. Acceptance uses actual SIGKILL at transfer/parse/pre-publication boundaries and injects a pointer-write failure. Do not delete `.state/` to recover a job.

## Contracts and consumer boundary

`contracts/v1/source-identity.json` and `locator.json` are byte-identical P2 copies. New contracts awaiting approval are `archive-manifest`, `kb-handoff`, `archive-locator`, `figure-occurrence`, `text-chunk` and `image-record`. `archive-locator` references the shared locator and adds byte/HTML ranges, EPUB image occurrences and saved-frame requested/actual-time facts. A missing measured frame time is null with reason `not found`.

The pure shared handoff conversion maps each normalized block exactly once, preserving original/translation/derived labels, parent/child IDs, complete embedding-input hashes, figure IDs, producing/source revisions and separate child/parent/context spans. The consumer must not split these records again. Generated portable PDFs enter the referenced blob inventory with a derivation mapping to their normalized inputs; their prose is not duplicated as another set of chunks. Book file descriptors can explicitly supply `derivation`, `transform_version` and `input_members`. Imported translation descriptors retain their explicit label; no model translation is generated here.

Before any future consumer imports a model, call `validate_release`: it checks schemas, safe role/path bindings, exact source/member/record/blob sets, byte counts/hashes, embedding inputs, span membership, original locators, figure occurrence pixels and privacy. The archive only emits pending handoffs. A completed state requires a matching source/revision, expected/actual counts, and saved/indexed consumer receipt; no consumer is implemented in P3.

Installed dependencies used are PyMuPDF, jsonschema and Pillow, plus the existing Domestika ffmpeg/ffprobe/yt-dlp/Chrome tools for its compatibility workflow. EPUB parsing uses standard-library ZIP/XML. No new package installation is required.
