import requests
import xml.etree.ElementTree as ET

from typing import List
from typing import Dict
from typing import Union

from finnews.parser import NewsParser


class CNBC():

    def __init__(self):

        self.url = 'https://www.cnbc.com/id/{topic_id}/device/rss/rss.html'
        self.topic_categories = {
            'top_news': '100003114',
        }
        self.news_parser = NewsParser(client='cnbc')

    def __repr__(self):
        return "<CnbcClient Connected: True'>"

    def _check_key(self, topic_id: str) -> str:

        if topic_id in self.topic_categories:

            full_url = self.url.format(
                topic_id=self.topic_categories[topic_id]
            )
            return full_url
        else:
            raise KeyError("The value you're searching for does not exist.")

    def news_feed(self, topic: str) -> List[Dict]:

        data = self.news_parser._make_request(
            url=self._check_key(topic_id=topic)
        )

        return data

    def investing_feeds(self, topic: str) -> List[Dict]:
        pass

    def blogs(self, topic: str) -> List[Dict]:
        pass

    def investing_feeds(self, topic: str) -> List[Dict]:
        pass

    def videos_and_tv(self, topic: str) -> List[Dict]:
        pass

    def tv_programs_europe(self, topic: str) -> List[Dict]:
        pass

    def tv_programs_asia(self, topic: str) -> List[Dict]:
        pass

    def _parse_results(self, raw_content: str) -> List[Dict]:
        pass
