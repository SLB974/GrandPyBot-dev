import requests


class WikiLoader:
    """Query Media Wiki api getting informations on location"""

    def __init__(self, lat, lng):
        self.__lat = lat
        self.__lng = lng

    @property
    def get_data(self):
        """getter method"""

        return self.__fetch_wiki(self.__fetch_title())

    def __fetch_title(self):
        """Find title and pageid and then find anecdote and url"""

        title = None
        id = None

        if self.__lat != None and self.__lng != None:

            param = {
                "action": "query",
                "list": "geosearch",
                "gsradius": 200,
                "gscoord": f"{self.__lat}|{self.__lng}",
                "gslimit": 1,
                "format": "json",
            }

            url = "https://fr.wikipedia.org/w/api.php"

            response = requests.get(url, params=param)

            if response.status_code == 200:
                response = response.json()

                if response["query"]["geosearch"]:
                    title = response["query"]["geosearch"][0]["title"]
                    id = response["query"]["geosearch"][0]["pageid"]
        return title, id

    def __fetch_wiki(self, references):

        data = {
            "anecdote": None,
            "url": None,
        }

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

            response = requests.get(url, params=param)

            if response.status_code == 200:
                response = response.json()

                id = str(id)

                if id in response["query"]["pages"]:

                    data["anecdote"] = response["query"]["pages"][id]["extract"]

                    data["url"] = response["query"]["pages"][id]["fullurl"]

        return data
