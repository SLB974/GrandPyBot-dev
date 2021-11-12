# GrandPyBot-dev

This app has been developped with Python-3.7.9

GrandPy is a bot that can search informations about any location and return (if founded):

  - the address of the location.
  - A map pointing on the location from Google maps.
  - an anecdote about the location from wikipedia.org.
  - a link to wikipedia page for further informations.
  
Please, make sure to configure an .env file containing constants :

  - GOOGLE_API_KEY = (your personnal google api key)
  - FLASK_DEBUG = True (for development features).
  
You can try the online finale version on (https://grandpy974.herokuapp.com/).

You can run the application by launching "main.py"

You can run tests suit by launching "python -m unittest app.core.tests.tests_unittest"

This web application is under MIT license.