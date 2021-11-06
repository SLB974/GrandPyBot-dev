from unittest.mock import MagicMock, patch
import pytest

from app.core.fetcher.fetch import GlobalFetcher

query = "Bonjour GrandPy, tu connais la tour eiffel ?"


@pytest.fixture
def fetcher():
    return GlobalFetcher(query)


def test_constructor():
    f = GlobalFetcher(query)
    assert isinstance(f, GlobalFetcher)


def test_get_data_calls_get_geocoder_data(fetcher):
    fetcher._GlobalFetcher__get_geocoder_data = MagicMock()
    actual = fetcher.get_data()
    fetcher._GlobalFetcher__get_geocoder_data.assert_called_once()


def test_get_data_calls_get_wikiloader_data(fetcher):
    fetcher._GlobalFetcher__get_wikiloader_data = MagicMock()
    actual = fetcher.get_data()
    fetcher._GlobalFetcher__get_wikiloader_data.assert_called_once()


def test_get_data_return_geocoder_and_wikiloader_data(fetcher):
    expected = {
        "grandpy_none": None,
        "grandpy_response": "Pour répondre à ta demande, voici ce que j'ai trouvé : ",
        "grandpy_catch_wiki": "Quelle coincidence, je connais très bien vois-tu... Savais-tu que...",
        "grandpy_next_query": "Alors, penses-tu pouvoir me soumettre un endroit plus difficile à présent ?",
        "map_link": "https://maps.googleapis.com/maps/api/staticmap?center=48.85837009999999,2.2944813&size=300x300&zoom=14&markers=color:red%7C48.85837009999999,2.2944813&key=AIzaSyDkeF5Xu-WxkLQWfA4TBXdcupRDi6KSeRY",
        "address": "Voici l'adresse : Champ de Mars, 5 Av. Anatole France, 75007 Paris, France",
        "wiki_response": "L'esplanade des Ouvriers-de-la-Tour-Eiffel est une voie située dans le 7e arrondissement de Paris, en France.\n\n\n== Situation et accès ==\nCette place piétonne se trouve sur le Champ-de-Mars, devant la tour Eiffel (côté ouest).\n\n\n== Origine du nom ==\n\n\n== Historique ==\n\n\n== Notes, sources et références ==\n\n\n=== Article connexe ===\nListe des voies du 7e arrondissement de Paris\nEsplanades de Paris Portail de Paris   Portail de la route",
        "wiki_link": "https://fr.wikipedia.org/wiki/Esplanade_des_Ouvriers-de-la-Tour-Eiffel",
    }

    actual = fetcher.get_data()

    assert expected == actual
