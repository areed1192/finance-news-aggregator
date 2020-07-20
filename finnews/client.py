import json

from typing import List
from typing import Dict
from typing import Union

from finnews.cnbc import CNBC


class News():

    def __init__(self):
        pass

    def __repr__(self):
        pass

    @property
    def cnbc(self) -> CNBC:
        return CNBC()

    def cnn_finance(self):
        pass

    def yahoo_finance(self):
        pass

    def save_to_file(self, content: List[Dict], file_name: str) -> None:

        file_name = r'samples\responses\{name}.jsonc'.format(name=file_name)

        with open(file_name, 'w+') as news_data:
            json.dump(obj=content, fp=news_data, indent=4)
