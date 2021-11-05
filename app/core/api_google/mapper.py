import requests

from app.config.settings import GOOGLE_API_KEY

# GOOGLE_API_KEY = "AIzaSyDkeF5Xu-WxkLQWfA4TBXdcupRDi6KSeRY"


class GeoCoder:
    """Query google places api for address and coordinates.
    # and generate google map link"""

    def __init__(self, query_list):
        self.input = "+".join(query_list)

    @property
    def get_data(self):
        """getter method"""

        return self.__fetch_coordinates()

    def __fetch_coordinates(self):
        """Query google api places"""

        param = {
            "input": self.input,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
            "key": GOOGLE_API_KEY,
        }

        data = {
            "address": None,
            "lat": None,
            "lng": None,
            "map_link": None,
        }

        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

        response = requests.get(url, params=param).json()

        if response["status"] == "OK":

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
