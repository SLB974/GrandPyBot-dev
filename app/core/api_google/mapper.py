import requests
import json

GOOGLE_API_KEY = "AIzaSyDkeF5Xu-WxkLQWfA4TBXdcupRDi6KSeRY"


class GeoCoder:
    """Query google places api for address and coordinates.
    and generate google map link"""

    def __init__(self, query_list):
        self.input = "+".join(query_list)
        self.__response = {"addresse": None, "lat": None, "lng": None, "map_link": None}

    def process(self):
        """Launch methods for fetching data"""

        self.fetch_coordinates()
        self.build_map_link()

    @property
    def get_response(self):
        """Getter method"""

        return self.__response

    def coordinates(self):
        """Generate usable coordinates for map link"""

        return ",".join([str(self.__response["lat"]), str(self.__response["lng"])])

    def fetch_coordinates(self):
        """Query google api places"""

        param = {
            "input": self.input,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
            "key": GOOGLE_API_KEY,
        }

        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

        response = requests.get(url, params=param).json()

        if response["status"] == "OK":

            self.__response["address"] = response["candidates"][0]["formatted_address"]
            self.__response["lat"] = response["candidates"][0]["geometry"]["location"]["lat"]
            self.__response["lng"] = response["candidates"][0]["geometry"]["location"]["lng"]

    def build_map_link(self):
        """generate usable map link"""

        self.__response["map_link"] = (
            "https://maps.googleapis.com/maps/api/staticmap?center="
            + self.coordinates()
            + "&size=400x400"
            + "&zoom=14"
            + "&markers=color:red%7C"
            + self.coordinates()
            + "&key="
            + GOOGLE_API_KEY
        )
