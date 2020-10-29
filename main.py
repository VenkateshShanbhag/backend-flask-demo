from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
client = MongoClient(port=27017)
db = client.m201

@app.route("/details", methods=["GET"])
def get_restaurant_details():
    return_details = {}
    count = 0
    restaurant_name = request.args.get("restaurant_name")
    details = db.restaurants.find({"name":restaurant_name})
    return dumps(details)


@app.route("/name", methods=["POST"])
def hello_world():

    try:
        var = request.get_json()
        for i in var.values():
            if i["name"] == "Venkatesh":
                print("posting to database")
        returnMsg = "Success!!"
    except:
        print("failuyre")
        returnMsg = "failed!!"
        #incase of failure

    return returnMsg


print(__name__)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
