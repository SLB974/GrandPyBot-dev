from unittest.mock import MagicMock
import pytest

from app.core.api_google.mapper import GeoCoder
from app.config.settings import GOOGLE_API_KEY

query = ["tour", "eiffel"]


@pytest.fixture
def geocoder():
    return GeoCoder(query)


def test_constructor():
    g = GeoCoder(query)
    assert isinstance(g, GeoCoder)


def test_get_data_return(geocoder):
    geocoder._GeoCoder__fetch_coordinates = MagicMock()
    geocoder._GeoCoder__fetch_coordinates.return_value = {
        "address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France",
        "lat": 48.85837009999999,
        "lng": 2.2944813,
        "map_link": "https://maps.googleapis.com/maps/api/staticmap?center=48.85837009999999,2.2944813&size=300x300&zoom=14&markers=color:red%7C48.85837009999999,2.2944813&key="
        + GOOGLE_API_KEY,
    }
    expected = {
        "address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France",
        "lat": 48.85837009999999,
        "lng": 2.2944813,
        "map_link": "https://maps.googleapis.com/maps/api/staticmap?center=48.85837009999999,2.2944813&size=300x300&zoom=14&markers=color:red%7C48.85837009999999,2.2944813&key="
        + GOOGLE_API_KEY,
    }
    actual = geocoder.get_data

    assert expected == actual


def test_get_data_method_calls_build_map_link(geocoder):
    geocoder._GeoCoder__build_map_link = MagicMock()
    actual = geocoder.get_data
    geocoder._GeoCoder__build_map_link.assert_called_once()


def test_get_data_method_calls_fetch_coordinates(geocoder):
    geocoder._GeoCoder__fetch_coordinates = MagicMock()
    actual = geocoder.get_data
    geocoder._GeoCoder__fetch_coordinates.assert_called_once()
