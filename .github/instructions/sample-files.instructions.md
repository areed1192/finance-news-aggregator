# Sample Files

Every new user-facing feature **must** ship with a sample file in `samples/`.

## Naming Convention

- `samples/use_<provider>_client.py` — matches the existing pattern (e.g. `use_cnbc_client.py`, `use_nasdaq_client.py`).
- If the feature extends an existing provider, add examples to the existing sample file instead of creating a new one.

## Required Structure

```python
from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the <Provider> News Client.
provider_client = news_client.<provider>

# ---------------------------------------------------------------------------
# Section: Describe what this block demonstrates.
# ---------------------------------------------------------------------------

# Fetch news for a specific topic.
top_news = provider_client.news_feed(topic='top_news')

# Fetch all available feeds.
all_feeds = provider_client.all_feeds()

# Save the data.
news_client.save_to_file(
    content=all_feeds,
    file_name='<provider>_all_feeds'
)
```

## Rules

1. **Comment each step** — a short inline comment before each call explaining what it does.
2. **No credentials needed** — this project uses random user agents internally; no API keys or user-agent strings are required.
3. **Import from `finnews.client`** — always start from `News()`, not internal modules. Imports from `finnews.news_enum` are acceptable when demonstrating enum-based topic selection.
4. **Cover the happy path** — demonstrate the primary use case per provider: fetch a specific topic, fetch all feeds, save results. Keep it concise (under ~80 lines).
5. **Section dividers** — use comment headers to separate logical sections when a sample covers multiple feed methods.
6. **Save output at the end** — call `news_client.save_to_file(content=..., file_name='...')` to show how results are persisted. The file is saved to the `samples/responses/` directory.
7. **Responses directory** — for each `save_to_file` call in the sample, a corresponding `.jsonc` file should exist in `samples/responses/`. These serve as reference output for documentation.

## When to Update vs. Create

| Scenario                                                     | Action                                    |
| ------------------------------------------------------------ | ----------------------------------------- |
| New news provider (e.g. `Bloomberg`)                         | Create `samples/use_<provider>_client.py` |
| New feed method on existing provider (e.g. `cnbc.podcasts()`)| Add a section to the existing sample file |
| Bug fix or internal refactor                                 | No sample file changes needed             |
