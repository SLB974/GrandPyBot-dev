from unittest.mock import MagicMock
import pytest

from app.core.api_wiki.wiki import WikiLoader

lat = 48.85837009999999
lng = 2.2944813


@pytest.fixture
def wikiloader():
    return WikiLoader(lat, lng)


def test_constructor():
    w = WikiLoader(lat, lng)
    assert isinstance(w, WikiLoader)


def test_get_data_return_calls_fetch_wiki(wikiloader):
    wikiloader._WikiLoader__fetch_wiki = MagicMock()
    actual = wikiloader.get_data
    wikiloader._WikiLoader__fetch_wiki.assert_called_once()


def test_fetch_title_return(wikiloader):
    expected = ("Esplanade des Ouvriers-de-la-Tour-Eiffel", 14307238)
    actual = wikiloader._WikiLoader__fetch_title()
    assert expected == actual


def test_fetch_wiki_return(wikiloader):
    wikiloader._WikiLoader__fetch_title = MagicMock()
    wikiloader._WikiLoader__fetch_title.return_value = ("Esplanade des Ouvriers-de-la-Tour-Eiffel", 14307238)

    expected = {
        "anecdote": "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France.\n\n\n== Situation et accès ==\nCette place piétonne se trouve sur le Champ-de-Mars, devant la tour Eiffel (côté ouest).\n\n\n== Origine du nom ==\n\n\n== Historique ==\n\n\n== Notes, sources et références ==\n\n\n=== Article connexe ===\nListe des voies du 7e arrondissement de Paris\nEsplanades de Paris Portail de Paris   Portail de la route",
        "url": "https://fr.wikipedia.org/wiki/Esplanade_des_Ouvriers-de-la-Tour-Eiffel",
    }

    actual = wikiloader._WikiLoader__fetch_wiki(("Esplanade des Ouvriers-de-la-Tour-Eiffel", 14307238))

    assert expected == actual
