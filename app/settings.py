from decouple import config

SECRET_KEY = config("SECRET_KEY", default="")
GOOGLE_API_KEY = config("GOOGLE_API_KEY", default="")
