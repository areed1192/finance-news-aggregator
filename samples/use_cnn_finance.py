from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the CNN Finance News Client.
cnn_finance_client = news_client.cnn_finance

# Grab the All Stories Feed.
content = cnn_finance_client.all_stories()
pprint(content)

# Grab the Top Stories Feed.
content = cnn_finance_client.top_stories()
pprint(content)

# Grab the Most Popular Feed.
content = cnn_finance_client.most_popular()
pprint(content)

# Grab the Companies Feed.
content = cnn_finance_client.companies()
pprint(content)

# Grab the International Feed.
content = cnn_finance_client.international()
pprint(content)

# Grab the Economy Feed.
content = cnn_finance_client.economy()
pprint(content)

# Grab the Video News Feed.
content = cnn_finance_client.video_news()
pprint(content)

# Grab the Media Feed.
content = cnn_finance_client.media()
pprint(content)

# Grab the Markets Feed.
content = cnn_finance_client.markets()
pprint(content)

# # Grab the Morning Buzz Feed - DOES NOT WORK.
# content = cnn_finance_client.morning_buzz()
# news_client.save_to_file(content=content, file_name='cnn_finance_morning_buzz')
# pprint(content)

# Grab the Technology Feed.
content = cnn_finance_client.techonology()
pprint(content)

# Grab the Personal Finance Feed.
content = cnn_finance_client.personal_finance()
pprint(content)

# Grab the Autos Feed.
content = cnn_finance_client.autos()
pprint(content)

# Grab the Colleges Feed.
content = cnn_finance_client.colleges()
pprint(content)

# Grab the Taxes Feed.
content = cnn_finance_client.taxes()
pprint(content)

# Grab the Funds Feed.
content = cnn_finance_client.funds()
pprint(content)

# Grab the Insurance Feed.
content = cnn_finance_client.insurance()
pprint(content)

# Grab the Retirement Feed.
content = cnn_finance_client.retirement()
pprint(content)

# Grab the Luxury Feed.
content = cnn_finance_client.luxury()
pprint(content)

# Grab the Lifestyle Feed.
content = cnn_finance_client.lifestyle()
pprint(content)

# Grab the Real Estate Feed.
content = cnn_finance_client.real_estate()
pprint(content)

# Grab the Small Business Feed.
content = cnn_finance_client.small_business()
pprint(content)
