from app.core.parser.parser import Parser
from app.core.grandpy.grandpy import GrandPy
from app.core.api_google.mapper import GeoCoder
from app.core.api_wiki.wiki import WikiLoader


class GlobalFetcher:
    """get usable data from Geocoder and WikiLoader"""

    def __init__(self, query):
        self.query = query
        self.__lat = None
        self.__lng = None

    def get_data(self):
        """Getter method"""

        geocoder_data = self.__get_geocoder_data()
        wikiloader_data = self.__get_wikiloader_data()
        return {**geocoder_data, **wikiloader_data}

    def __get_geocoder_data(self):
        """get data from GeoCoder if usable query"""

        data = {
            "grandpy_none": None,
            "grandpy_response": None,
            "grandpy_catch_wiki": None,
            "grandpy_next_query": None,
            "map_link": None,
            "address": None,
        }

        parser = Parser(self.query)
        grandpy = GrandPy()

        if parser.clean_string() == "":
            data["grandpy_none"] = grandpy.empty_response()
            return data

        geocoder = GeoCoder(parser.clean_string())

        if geocoder.get_data["address"] == None:
            data["grandpy_none"] = grandpy.error_response()
            return data

        data["grandpy_response"] = grandpy.positive_response()
        data["grandpy_catch_wiki"] = grandpy.anecdote()
        data["address"] = "Voici l'adresse : " + geocoder.get_data["address"]
        data["map_link"] = geocoder.get_data["map_link"]
        data["grandpy_next_query"] = grandpy.next_query()

        self.__lat = geocoder.get_data["lat"]
        self.__lng = geocoder.get_data["lng"]

        return data

    def __get_wikiloader_data(self):
        """Get data from WikiLoader if usabel lat and lng"""

        data = {
            "wiki_response": None,
            "wiki_link": None,
        }

        if self.__lat != None and self.__lng != None:
            wikiloader = WikiLoader(self.__lat, self.__lng)
            data["wiki_response"] = wikiloader.get_data["anecdote"]
            data["wiki_link"] = wikiloader.get_data["url"]

        return data
