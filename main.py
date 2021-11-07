from app.config.settings import FLASK_DEBUG
from app import app

if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG)
