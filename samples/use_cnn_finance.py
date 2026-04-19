"""Sample script demonstrating the CNN Finance news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed

# Create a new instance of the News Client.
news_client = News()

# Grab the CNN Finance News Client.
cnn_finance_client = news_client.cnn_finance

# ---------------------------------------------------------------------------
# Section: List available feeds.
# ---------------------------------------------------------------------------

# Print the available feed methods.
print("Available feeds:", cnn_finance_client.feeds)

# ---------------------------------------------------------------------------
# Section: Fetch a feed and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the Top Stories Feed.
top_stories = cnn_finance_client.top_stories()

# Wrap the results in a NewsFeed.
feed = NewsFeed.from_dicts(top_stories, source='cnn_finance')
print(f"\nTop stories: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Convert a single result to a NewsArticle.
if top_stories:
    article = NewsArticle.from_dict(top_stories[0], source='cnn_finance')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")

# ---------------------------------------------------------------------------
# Section: Fetch additional feeds.
# ---------------------------------------------------------------------------

# Grab the All Stories Feed.
all_stories = cnn_finance_client.all_stories()
pprint(all_stories)

# Grab the Most Popular Feed.
most_popular = cnn_finance_client.most_popular()
pprint(most_popular)

# Grab the Companies Feed.
companies = cnn_finance_client.companies()
pprint(companies)

# Grab the International Feed.
international = cnn_finance_client.international()
pprint(international)

# Grab the Economy Feed.
economy = cnn_finance_client.economy()
pprint(economy)

# Grab the Video News Feed.
video_news = cnn_finance_client.video_news()
pprint(video_news)

# Grab the Media Feed.
media = cnn_finance_client.media()
pprint(media)

# Grab the Markets Feed.
markets = cnn_finance_client.markets()
pprint(markets)

# Grab the Technology Feed.
technology = cnn_finance_client.technology()
pprint(technology)

# Grab the Personal Finance Feed.
personal_finance = cnn_finance_client.personal_finance()
pprint(personal_finance)

# Grab the Autos Feed.
autos = cnn_finance_client.autos()
pprint(autos)

# Grab the Colleges Feed.
colleges = cnn_finance_client.colleges()
pprint(colleges)

# Grab the Taxes Feed.
taxes = cnn_finance_client.taxes()
pprint(taxes)

# Grab the Funds Feed.
funds = cnn_finance_client.funds()
pprint(funds)

# Grab the Insurance Feed.
insurance = cnn_finance_client.insurance()
pprint(insurance)

# Grab the Retirement Feed.
retirement = cnn_finance_client.retirement()
pprint(retirement)

# Grab the Luxury Feed.
luxury = cnn_finance_client.luxury()
pprint(luxury)

# Grab the Lifestyle Feed.
lifestyle = cnn_finance_client.lifestyle()
pprint(lifestyle)

# Grab the Real Estate Feed.
real_estate = cnn_finance_client.real_estate()
pprint(real_estate)

# Grab the Small Business Feed.
small_business = cnn_finance_client.small_business()
pprint(small_business)
