from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.city


def get_restaurant_details(restaurant_name):
    details = db.restaurants.find({"name": restaurant_name})
    return details

def put_restaurant_details(details):
    try:
        id = db.restaurants.insert_one(details)
        res = "inserted successfully!"
    except:
        res = "not able to insert! Please check again"
    return res
