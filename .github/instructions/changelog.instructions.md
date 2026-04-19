# Changelog

Every user-visible change **must** be recorded in `CHANGELOG.md` before the work is considered complete.

## Format

This project follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

All unreleased work goes under `## [Unreleased]`. Entries are grouped by type:

```markdown
## [Unreleased]

### Added

- New features.

### Changed

- Changes to existing functionality.

### Fixed

- Bug fixes.

### Removed

- Removed features.
```

## Entry Format

Each entry follows this pattern:

```markdown
- **<file or module>**: Brief description of what was added/changed.
  - Sub-bullet for important details (methods, properties, behavior).
  - Another sub-bullet if needed.
```

### Examples

```markdown
- **finnews/parser.py**: Added `timeout=10` to `requests.get()` in `_make_request`.
- **finnews/market_watch.py**: Fixed `_check_key` format bug — `topic_id=` → `topic=`.
- **tests/test_parser.py**: 12 unit tests for `NewsParser` parsing and request logic.
  - 7 tests for `_parse_response`: basic parsing, namespace stripping, empty feeds.
  - 5 tests for `_make_request`: timeout, params, HTTP errors, user-agent header.
```

## Rules

1. **Bold the file path** — `**finnews/parser.py**:` prefix identifies where the change lives.
2. **One entry per logical change** — don't combine unrelated changes into one bullet.
3. **Include test files** — new test files get their own `### Added` entry with the test count.
4. **Include sample files** — new or updated sample files get their own entry.
5. **Use the right section** — new features → `Added`, behavior changes → `Changed`, bug fixes → `Fixed`.
6. **Never edit released sections** — only modify `## [Unreleased]`.
7. **Update at the end** — add changelog entries as the final step after code and tests pass.

## What Doesn't Need a Changelog Entry

- Internal refactors with no API change
- Comment-only changes
- CI/tooling config changes (unless they affect users)

## Releasing a Version

When publishing a new version:

1. Replace `## [Unreleased]` with `## [x.y.z] - YYYY-MM-DD` (e.g. `## [0.2.0] - 2026-04-19`).
2. Update `version` in `pyproject.toml` to match.
3. Optionally add a new empty `## [Unreleased]` section above the release for future work.
4. Never edit a previously released section after publishing.
