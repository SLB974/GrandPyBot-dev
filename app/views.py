from flask import Flask, render_template, jsonify, url_for, request

from app.core.fetcher.fetch import GlobalFetcher
from app.core.grandpy.grandpy import GrandPy

app = Flask(__name__)

# app.config.from_object("settings")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/intro", methods=["GET"])
def intro():
    grandpy = GrandPy()
    response = {"intro": grandpy.intro_phrase()}
    return response


@app.route("/ajax", methods=["POST"])
def manage_query():
    data = request.get_json(force=True)
    fetcher = GlobalFetcher(data)
    fetcher.process()
    return fetcher.get_data()


if __name__ == "__main__":
    app.run()
