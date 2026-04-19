# Pylint

All Python files must pass pylint with a **10.00/10** score before work is considered complete.

## Running Locally

```bash
pip install pylint
python -m pylint <package>/ tests/ --max-line-length=127
```

Check `pyproject.toml` for any project-level pylint configuration (e.g. disabled rules) and honour those settings when running locally.

## Docstrings

Every module, class, and public function/method must have a docstring.

- **Modules**: Add a one-line or multi-line docstring at the top of every `.py` file describing its purpose.
- **Classes**: Describe what the class represents and its high-level usage.
- **Public methods/functions**: Describe arguments, return values, and raised exceptions.
- **Test files**: A module-level docstring is sufficient; individual test methods should have a short description of what they verify.

```python
"""Client module for accessing the News aggregator API."""

class NewsClient:
    """Facade that provides access to individual news provider clients."""

    def fetch(self, topic: str) -> list[dict]:
        """Fetch articles for the given topic.

        Args:
            topic: The topic identifier to query.

        Returns:
            A list of article dictionaries.
        """
```

pylint enforces this via `C0114` (missing-module-docstring), `C0115` (missing-class-docstring), and `C0116` (missing-function-docstring). Do not disable these rules.

## Inline Suppression Rules

Use inline `# pylint: disable=<rule>` comments **only** when a warning is a deliberate design choice. Place the comment on the specific line or class it applies to — avoid file-level disables unless the entire file genuinely needs them.

Do **not** add new inline disables without justification. Fix the code first. Only suppress if the warning conflicts with an intentional design decision, and add a brief comment explaining why.

```python
class MyFacade:  # pylint: disable=too-many-instance-attributes  # one attr per provider
```

## Common Warnings to Fix

### R1705 `no-else-return`

Remove the `else` block after a `return` statement — the code after the `if` already implies the else path.

```python
# Bad
if condition:
    return value
else:
    raise SomeError()

# Good
if condition:
    return value
raise SomeError()
```

### C0415 `import-outside-toplevel`

Move all imports to the top of the file. Do not use inline `import` statements inside functions or methods.

### W0212 `protected-access`

Do not call `_private` methods from outside the owning class. If a method is used externally, rename it to be public (drop the underscore). The only acceptable exception is in test files that need to exercise internal helpers — suppress with a file-level `# pylint: disable=protected-access` and a comment.

### W0201 `attribute-defined-outside-init`

In test classes, use local variables instead of `self.xxx` for values that are not set in `setUp`. Only `setUp`-defined attributes should use `self`.

### W3101 `missing-timeout`

Always pass `timeout=` to `requests.get()` / `requests.post()` and similar calls to prevent indefinite hangs.

### R0801 `duplicate-code`

If structural duplication is inherent to the design (e.g. multiple provider classes following the same pattern), disable at the project level in `pyproject.toml` rather than sprinkling inline disables.
