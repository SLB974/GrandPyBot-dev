from unittest.mock import patch, MagicMock
from unittest import TestCase

from app.core.fetcher.fetch import GlobalFetcher

user_query = "Bonjour GrandPy, tu connais la tour eiffel ?"


def mocked_geocoder_response():
    """returns geocoder fake response"""

    return {
        "grandpy_none": None,
        "grandpy_response": "Voici ce que j'ai trouvé :",
        "grandpy_catch_wiki": "J'ai vécu là-bas tu sais ?",
        "grandpy_next_query": "Alors on fait quoi maintenant ?",
        "map_link": "un lien",
        "address": "une adresse",
    }


def mocked_wikiloader_response():
    """returns wikiloader fake response"""

    return {"anecdote": "Une anecdote", "url": "un url"}


class GlobalFetcherTestCase(TestCase):

    globalfetcher = GlobalFetcher(user_query)

    @patch.multiple(
        "app.core.fetcher.fetch.GlobalFetcher",
        _GlobalFetcher__get_geocoder_data=MagicMock(return_value=mocked_geocoder_response()),
        _GlobalFetcher__get_wikiloader_data=MagicMock(return_value=mocked_wikiloader_response()),
    )
    def test_get_proper_response_with_usable_query(self):
        expected = {**mocked_geocoder_response(), **mocked_wikiloader_response()}
        self.assertEqual(self.globalfetcher.get_data(), expected)
