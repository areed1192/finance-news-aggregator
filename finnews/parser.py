import requests
import xml.etree.ElementTree as ET

from typing import List
from typing import Dict
from typing import Union


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
            'cnbc': './channel/item'
        }

        self.namespaces = {
            'cnbc': '{http://search.cnbc.com/rss/2.0/modules/siteContentMetadata}'
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
        """Used to make a request for each of the news clients.

        Arguments:
        ----
        url (str): The URL to request.

        Returns:
        ----
        List[Dict]: A list of news items objects.
        """

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
