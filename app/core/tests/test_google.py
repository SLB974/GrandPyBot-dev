from unittest.mock import Mock, patch
from unittest import TestCase

from app.core.api_google.mapper import GeoCoder
from app.config.settings import GOOGLE_API_KEY


def mocked_google_place_response_tour_eiffel():
    """method that returns google_place_response with tour eiffel"""

    return {
        "candidates": [
            {
                "formatted_address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France",
                "geometry": {
                    "location": {"lat": 48.85837009999999, "lng": 2.2944813},
                    "viewport": {
                        "northeast": {"lat": 48.85974697989273, "lng": 2.29610765},
                        "southwest": {"lat": 48.85704732010728, "lng": 2.29251745},
                    },
                },
            }
        ],
        "status": "OK",
    }


def mocked_google_place_response_none():
    """method that returns google_place_response with improper input"""

    return {"candidates": [], "status": "INVALID_REQUEST"}


class GeoCoderTestCase(TestCase):

    geocoder = GeoCoder(["tour", "eiffel"])

    def test_get_data_proper_response(self):
        with patch("app.core.api_google.mapper.GeoCoder.google_place_response") as mocked_method:
            mocked_method.return_value = mocked_google_place_response_tour_eiffel()
            expected = {
                "address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France",
                "lat": 48.85837009999999,
                "lng": 2.2944813,
                "map_link": "https://maps.googleapis.com/maps/api/staticmap?center=48.85837009999999,2.2944813&size=300x300&zoom=14&markers=color:red%7C48.85837009999999,2.2944813&key="
                + GOOGLE_API_KEY,
            }

            self.assertEqual(self.geocoder.get_data, expected)

    def test_get_data_response_none(self):
        with patch("app.core.api_google.mapper.GeoCoder.google_place_response") as mocked_method:
            mocked_method.return_value = mocked_google_place_response_none()
            expected = {"address": None, "lat": None, "lng": None, "map_link": None}

            self.assertEqual(self.geocoder.get_data, expected)
