from decouple import config

GOOGLE_API_KEY = config("GOOGLE_API_KEY")
FLASK_DEBUG = config("FLASK_DEBUG", default=True, cast=bool)
