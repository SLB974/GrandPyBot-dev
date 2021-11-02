# coding: utf-8
from unidecode import unidecode
import re

from .utils import stop_words


class Parser:
    """Parse user's query"""

    def __init__(self, user_query):
        self.user_query = user_query

    def clean_string(self):
        """remove accents, upper and punctuation
        and split into list
        compare to stop_words reference and remove found items"""

        cleaned = unidecode(self.user_query).lower()
        cleaned = re.compile("\w+").findall(cleaned)
        return [item for item in cleaned if item not in stop_words]
