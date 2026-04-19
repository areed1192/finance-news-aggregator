# Linting

All Python files must pass lint checks before work is considered complete.

## Tooling

This project uses **flake8** for linting. CI runs flake8 on every push and pull request via `.github/workflows/python-package.yml`.

### CI lint configuration

- **Fatal errors**: `E9,F63,F7,F82` (syntax errors, undefined names) — these fail the build.
- **Warnings**: All other rules run with `--exit-zero` and `--max-complexity=10 --max-line-length=127`.

Install locally with:

```bash
pip install flake8
```

## Common Rules to Watch For

### Unused imports

- Remove any import that is not used in the file.
- `TYPE_CHECKING` imports are fine — they're used for type hints only.

### Line length

- Target **127 characters** per line (matching CI config). Break long strings, dict literals, and function signatures across multiple lines.

### Import ordering

- Standard library first, then third-party, then local `finnews.*` imports.
- Separate groups with a blank line.

```python
import json
import logging
from typing import List, Dict

import requests
from fake_useragent import UserAgent

from finnews.parser import NewsParser
from finnews.fields import cnbc_rss_feeds_id
```

### Type hints

- Use `from __future__ import annotations` at the top of modules that use `X | Y` union syntax.
- Use `TYPE_CHECKING` guard for imports only needed for type hints to avoid circular imports.

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from finnews.parser import NewsParser
```

## Running Lint Locally

```bash
# Fatal errors only (same as CI gate):
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Full warnings report:
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
```

### f-string formatting

- Prefer f-strings over `.format()` or `%` formatting.
- Use `!r` for values that should show their repr: `f"Got: {value!r}"`.

## Validation Workflow

After completing any code change:

1. Check for lint errors in modified files using the editor's problem panel.
2. Fix all errors and warnings before committing.
3. If a new per-file disable is genuinely needed, document why in a comment.

## Files That Must Be Lint-Clean

- All files under `edgar/` (source code)
- All files under `tests/` (test code)
- Sample files under `samples/` are best-effort but should still be clean.
