import requests
import xml.etree.ElementTree as ET

from typing import List
from typing import Dict
from typing import Union


class NewsParser():

    def __init__(self, client: str):

        self.client = client
        self.paths = {
            'cnbc': './channel/item'
        }

        self.namespaces = {
            'cnbc': '{http://search.cnbc.com/rss/2.0/modules/siteContentMetadata}'
        }

    def _parse_response(self, response_content: str) -> List[Dict]:

        # Parse the text.
        root = ET.fromstring(response_content)
        entries = []

        # Grab the path.
        path = self.paths[self.client]

        # Find all the news items.
        for news_item in root.findall(path):

            # Initialize a new dictionary.
            item_dict = {}

            # Loop through each element.
            for news_item_element in news_item.iter():
                
                # Replace the namespace.
                replace_path = self.namespaces[self.client]

                # Clean the tag.
                news_tag = news_item_element.tag.replace(replace_path, "")

                # Grab the text.
                news_value = news_item_element.text.strip()

                # Store it.
                item_dict[news_tag] = news_value

            entries.append(item_dict)

        return entries

    def _make_request(self, url: str) -> List[Dict]:


        # Define a new session.
        new_session = requests.Session()
        new_session.verify = True

        # Prepare the request.
        new_request = requests.Request(
            method='GET',
            url=url
        ).prepare()

        # Send the request.
        response: requests.Response = new_session.send(
            request=new_request
        )

        # Parse the response.
        data = self._parse_response(response_content=response.content)

        return data
