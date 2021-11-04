from ..parser.parser import Parser
from ..grandpy.grandpy import GrandPy
from ..api_google.mapper import GeoCoder
from ..api_wiki.wiki import WikiLoader


class GlobalFetcher:
    def __init__(self, query):
        self.query = query
        self.__response = {
            "grandpy_none": None,
            "grandpy_response": None,
            "grandpy_catch_wiki": None,
            "grandpy_next_query": None,
            "map_link": None,
            "address": None,
            "wiki_response": None,
            "wiki_link": None,
        }

    def process(self):
        self.fetch_data()

    def get_data(self):
        return self.__response

    def fetch_data(self):

        parser = Parser(self.query)
        grandpy = GrandPy()

        if parser.clean_string() == "":
            self.__response["grandpy_none"] = grandpy.empty_response()
            return

        geocoder = GeoCoder(parser.clean_string())
        geocoder.process()

        if geocoder.get_response["address"] == None:
            self.__response["grandpy_none"] = grandpy.error_response()
            return

        self.__response["grandpy_response"] = grandpy.positive_response()
        self.__response["grandpy_catch_wiki"] = grandpy.anecdote()
        self.__response["address"] = "Voici l'adresse : " + geocoder.get_response["address"]
        self.__response["map_link"] = geocoder.get_response["map_link"]
        self.__response["grandpy_next_query"] = grandpy.next_query()

        wikiloader = WikiLoader(geocoder.get_response["lat"], geocoder.get_response["lng"])
        wikiloader.process()
        self.__response["wiki_response"] = wikiloader.get_response["anecdote"]
        self.__response["wiki_link"] = wikiloader.get_response["url"]
