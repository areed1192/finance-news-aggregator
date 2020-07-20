import requests
import xml.etree.ElementTree as ET

from typing import List
from typing import Dict
from typing import Union


class CNBC():

    def __init__(self):

        self.url = 'https://www.cnbc.com/id/{topic_id}/device/rss/rss.html'
        self.topic_categories = {
            'top_news': '100003114',
        }

    def __repr__(self):
        return "<CnbcClient Connected: True'>"

    def _parse_response(self, response_content: str) -> List[Dict]:

        # Parse the text.
        root = ET.fromstring(response_content)
        entries = []

        # Find all the news items.
        for news_item in root.findall('./channel/item'):

            item_dict = {}

            for news_item_element in news_item.iter():

                news_tag = news_item_element.tag.replace('{http://search.cnbc.com/rss/2.0/modules/siteContentMetadata}','')
                news_value = news_item_element.text.strip()
                item_dict[news_tag] = news_value

            entries.append(item_dict)

        return entries

    def _make_request(self, topic_id: str) -> List[Dict]:

        if topic_id in self.topic_categories:
            
            full_url = self.url.format(
                topic_id=self.topic_categories[topic_id]
            )

        else:
            raise KeyError("The value you're searching for does not exist.")
        
        # Define a new session.
        new_session = requests.Session()
        new_session.verify = True

        # Prepare the request.
        new_request = requests.Request(
            method='GET',
            url=full_url
        ).prepare()

        # Send the request.
        response: requests.Response = new_session.send(
            request=new_request
        )

        # Parse the response.
        data = self._parse_response(response_content=response.content)

        return data

    def news_feed(self, topic: str) -> List[Dict]:

        data = self._make_request(topic_id=topic)

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
