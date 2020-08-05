import requests
import xml.etree.ElementTree as ET

from typing import List
from typing import Dict
from typing import Union

from fake_useragent import UserAgent


class NewsParser():

    """Serves as the parser for each of the
    news clients."""

    def __init__(self, client: str) -> None:
        """Initializes the new parser client.

        Overview:
        ----
        To help standardize the parser process the
        `NewsParser` client is used to help make the
        request, parse the response, and organize the
        results for each of the news client.

        Arguments:
        ----
        client (str): The ID of the client you wish to use
            the parser for.

        Usage:
        ----
            >>> self.news_parser = NewsParser(client='cnbc')
        """

        self.client = client
        self.paths = {
            'cnbc': './channel/item',
            'nasdaq': './channel/item',
            'market_watch': './channel/item',
            'sp_global': '.channel/item'
        }

        self.namespaces = {
            'cnbc': ['{http://search.cnbc.com/rss/2.0/modules/siteContentMetadata}'],
            'nasdaq': [
                '{http://purl.org/dc/elements/1.1/}',
                '{http://nasdaq.com/reference/feeds/1.0}',
                '{http://purl.org/dc/elements/1.1/}'
            ],
            'market_watch':[
                '{http://rssnamespace.org/feedburner/ext/1.0}'
            ],
            'sp_global':[
                ''
            ]
        }

    def _parse_response(self, response_content: str) -> List[Dict]:
        """Parses the text content from a request and returns the news item collection.

        Arguments:
        ----
        response_content (str): The raw XML content from the RSS feed that
            needs to be parsed.

        Returns:
        ----
        List[Dict]: A list of news items objects.
        """

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

                # Grab the news tag.
                news_tag: str = news_item_element.tag

                # Replace the namespace.
                for path in self.namespaces[self.client]:

                    # Clean the tag.
                    news_tag = news_tag.replace(path, "")

                # Grab the text.
                if news_item_element.text:
                    news_value = news_item_element.text.strip()
                else:
                    news_value = ""

                # Store it.
                item_dict[news_tag] = news_value

            entries.append(item_dict)

        return entries

    def _make_request(self, url: str, params: dict = None) -> List[Dict]:
        """Used to make a request for each of the news clients.

        Arguments:
        ----
        url (str): The URL to request.

        params (dict): The paramters to pass through to the request.

        Returns:
        ----
        List[Dict]: A list of news items objects.
        """

        # Fake the headers.
        headers = {
            'user-agent': UserAgent().edge
        }

        # Grab the response.
        response = requests.get(url=url, headers=headers, params=params)

        # Parse the response.
        data = self._parse_response(response_content=response.content)

        return data
