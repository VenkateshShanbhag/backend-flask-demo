# from flask import Flask, request

from bson.json_util import dumps
from src.utility.mongoutility import get_restaurant_details,put_restaurant_details

import flask

app = flask.Flask(__name__)


@app.route("/details", methods=["GET","POST"])
def restaurant_details():
    if flask.request.method == 'GET':
        restaurant_name = flask.request.args.get("restaurant_name")
        details = get_restaurant_details(restaurant_name)
        return dumps(details)
    if flask.request.method == 'POST':
        details = flask.request.get_json()
        res = put_restaurant_details(details)
        return res

print(__name__)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
