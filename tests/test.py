import requests
from fake_useragent import UserAgent


# Fake the headers.
headers = {
    'user-agent': UserAgent().edge
}

content = requests.get(url='https://www.nasdaq.com/feed/nasdaq-original/rss.xml', headers=headers)

print(content.text)