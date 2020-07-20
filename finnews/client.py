
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

