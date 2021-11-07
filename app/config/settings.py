from decouple import config

GOOGLE_API_KEY = config("GOOGLE_API_KEY", default="AIzaSyDkeF5Xu-WxkLQWfA4TBXdcupRDi6KSeRY")
FLASK_DEBUG = config("FLASK_DEBUG", default=True)
