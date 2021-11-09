import requests
import json


class WikiLoader:
    """Query Media Wiki api getting informations on location"""

    def __init__(self, lat, lng):
        self.__lat = lat
        self.__lng = lng

    @property
    def get_data(self):
        """getter method"""

        return self.get_wiki_anecdote(self.get_title())

        # return self.__fetch_wiki(self.__fetch_title())

    def wiki_response(self, url, param):
        """Query wikipedia api and return json"""

        response = requests.get(url, param)

        if response.status_code == 200:
            return response.json()

        return None

    def get_title(self):
        """Fetch page title and page id"""

        title = None
        pageid = None

        if self.__lat != None and self.__lng != None:

            param = {
                "action": "query",
                "list": "geosearch",
                "gsradius": 1500,
                "gscoord": f"{self.__lat}|{self.__lng}",
                "gslimit": 1,
                "format": "json",
            }

            url = "https://fr.wikipedia.org/w/api.php"

            response = self.wiki_response(url, param)

            with open("json2.json", "w") as f:
                json.dump(response, f)

            if response and response["query"]["geosearch"]:
                title = response["query"]["geosearch"][0]["title"]
                pageid = response["query"]["geosearch"][0]["pageid"]

        return title, pageid

    def get_wiki_anecdote(self, references):
        """Fetch anecdote and url"""

        data = {"anecdote": None, "url": None}

        title, id = references[0], references[1]

        if title != None and id != None:

            param = {
                "action": "query",
                "prop": "extracts|info",
                "exchars": 1000,
                "titles": title,
                "inprop": "url",
                "explaintext": "",
                "format": "json",
            }

            url = "https://fr.wikipedia.org/w/api.php"

            id = str(id)

            response = self.wiki_response(url, param)
            with open("json3.json", "w") as f:
                json.dump(response, f)

            if response and response["query"]["pages"]:
                data["anecdote"] = response["query"]["pages"][id]["extract"]
                data["url"] = response["query"]["pages"][id]["fullurl"]

        return data
