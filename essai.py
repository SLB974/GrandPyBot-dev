from app.core.fetcher.fetch import GlobalFetcher
from app.core.api_wiki.wiki import WikiLoader

query = "Bonjour GrandPy, tu connais la tour eiffel ?"

fetcher = GlobalFetcher(query)
print(fetcher.get_data())
