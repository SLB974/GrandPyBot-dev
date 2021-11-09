import requests

from app.config.settings import GOOGLE_API_KEY


class GeoCoder:
    """Query google places api for address and coordinates.
    and generate google map link"""

    def __init__(self, query_list):
        self.input = "+".join(query_list)

    @property
    def get_data(self):
        """getter method"""

        return self.get_coordinates()

    def google_place_response(self):
        """Query google api place and return json object"""

        param = {
            "input": self.input,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
            "key": GOOGLE_API_KEY,
        }

        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

        response = requests.get(url, params=param)

        if response.status_code == 200:
            return response.json()

        return None

    def get_coordinates(self):
        """get data from http response"""

        data = {
            "address": None,
            "lat": None,
            "lng": None,
            "map_link": None,
        }

        response = self.google_place_response()

        if response and response["candidates"]:
            data["address"] = response["candidates"][0]["formatted_address"]
            data["lat"] = response["candidates"][0]["geometry"]["location"]["lat"]
            data["lng"] = response["candidates"][0]["geometry"]["location"]["lng"]

            coordinates = ",".join([str(data["lat"]), str(data["lng"])])
            data["map_link"] = self.__build_map_link(coordinates)

        return data

    def __build_map_link(self, coordinates):
        """generate usable map link"""

        return (
            "https://maps.googleapis.com/maps/api/staticmap?center="
            + coordinates
            + "&size=300x300"
            + "&zoom=14"
            + "&markers=color:red%7C"
            + coordinates
            + "&key="
            + GOOGLE_API_KEY
        )
