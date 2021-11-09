from unittest.mock import patch
from unittest import TestCase

from app.core.api_wiki.wiki import WikiLoader

lat = 48.85837009999999
lng = 2.2944813


def mocked_wiki_title_response_tour_eiffel():
    """returns wiki response for title and pageid"""
    return {
        "batchcomplete": "",
        "query": {
            "geosearch": [
                {
                    "pageid": 14307238,
                    "ns": 0,
                    "title": "Esplanade des Ouvriers-de-la-Tour-Eiffel",
                    "lat": 48.85834,
                    "lon": 2.29445,
                    "dist": 4.1,
                    "primary": "",
                }
            ]
        },
    }


def mocked_wiki_anecdote_response_tour_eiffel():
    """returns wiki response for anecdote and url"""

    return {
        "batchcomplete": "",
        "query": {
            "pages": {
                "14307238": {
                    "pageid": 14307238,
                    "ns": 0,
                    "title": "Esplanade des Ouvriers-de-la-Tour-Eiffel",
                    "extract": "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie situ\u00e9e dans le 7e arrondissement de Paris, en France.\n\n\n== Situation et acc\u00e8s ==\nCette place pi\u00e9tonne se trouve sur le Champ-de-Mars, devant la tour Eiffel (c\u00f4t\u00e9 ouest).\n\n\n== Origine du nom ==\n\n\n== Historique ==\n\n\n== Notes, sources et r\u00e9f\u00e9rences ==\n\n\n=== Article connexe ===\nListe des voies du 7e arrondissement de Paris\nEsplanades de Paris Portail de Paris   Portail de la route",
                    "contentmodel": "wikitext",
                    "pagelanguage": "fr",
                    "pagelanguagehtmlcode": "fr",
                    "pagelanguagedir": "ltr",
                    "touched": "2021-10-23T09:22:47Z",
                    "lastrevid": 187360603,
                    "length": 1493,
                    "fullurl": "https://fr.wikipedia.org/wiki/Esplanade_des_Ouvriers-de-la-Tour-Eiffel",
                    "editurl": "https://fr.wikipedia.org/w/index.php?title=Esplanade_des_Ouvriers-de-la-Tour-Eiffel&action=edit",
                    "canonicalurl": "https://fr.wikipedia.org/wiki/Esplanade_des_Ouvriers-de-la-Tour-Eiffel",
                }
            }
        },
    }


class WikiLoaderTestCase(TestCase):

    wikiloader = WikiLoader(lat, lng)

    def test_get_title_proper_response_tour_eiffel(self):
        with patch("app.core.api_wiki.wiki.WikiLoader._WikiLoader__wiki_response") as mocked_method:
            mocked_method.return_value = mocked_wiki_title_response_tour_eiffel()
            expected = ("Esplanade des Ouvriers-de-la-Tour-Eiffel", 14307238)

            self.assertEqual(self.wikiloader._WikiLoader__get_title(), expected)

    def test_get_wiki_anecdote_proper_response_tour_eiffel(self):
        with patch("app.core.api_wiki.wiki.WikiLoader._WikiLoader__wiki_response") as mocked_method:
            mocked_method.return_value = mocked_wiki_anecdote_response_tour_eiffel()
            expected = {
                "anecdote": "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie situ\u00e9e dans le 7e arrondissement de Paris, en France.\n\n\n== Situation et acc\u00e8s ==\nCette place pi\u00e9tonne se trouve sur le Champ-de-Mars, devant la tour Eiffel (c\u00f4t\u00e9 ouest).\n\n\n== Origine du nom ==\n\n\n== Historique ==\n\n\n== Notes, sources et r\u00e9f\u00e9rences ==\n\n\n=== Article connexe ===\nListe des voies du 7e arrondissement de Paris\nEsplanades de Paris Portail de Paris   Portail de la route",
                "url": "https://fr.wikipedia.org/wiki/Esplanade_des_Ouvriers-de-la-Tour-Eiffel",
            }

            self.assertEqual(
                self.wikiloader._WikiLoader__get_wiki_anecdote(("Esplanade des Ouvriers-de-la-Tour-Eiffel", 14307238)),
                expected,
            )
