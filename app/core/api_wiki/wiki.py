import requests
import json


class WikiLoader:
    """Query Media Wiki api getting informations on location"""

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.__response = {"title": None, "pageid": None, "anecdote": None, "url": None}

    def process(self):
        self.fetch_wiki()
        self.fetch_content()

    @property
    def get_response(self):
        return self.__response

    def fetch_wiki(self):
        """Find title and pageid"""

        param = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 200,
            "gscoord": f"{self.lat}|{self.lng}",
            "gslimit": 1,
            "format": "json",
        }

        url = "https://fr.wikipedia.org/w/api.php"

        response = requests.get(url, params=param)

        if response.status_code == 200:
            response = response.json()

            if response["query"]["geosearch"]:
                self.__response["title"] = response["query"]["geosearch"][0]["title"]
                self.__response["pageid"] = response["query"]["geosearch"][0]["pageid"]

    def fetch_content(self):
        """find full text anecdote"""

        param = {
            "action": "query",
            "prop": "extracts|info",
            "exchars": 1200,
            "titles": self.__response["title"],
            "inprop": "url",
            "explaintext": "",
            "format": "json",
        }

        url = "https://fr.wikipedia.org/w/api.php"

        response = requests.get(url, params=param)

        if response.status_code == 200:
            response = response.json()

            id = str(self.__response["pageid"])

            if id in response["query"]["pages"]:

                self.__response["anecdote"] = response["query"]["pages"][id]["extract"]

                self.__response["url"] = response["query"]["pages"][id]["fullurl"]
