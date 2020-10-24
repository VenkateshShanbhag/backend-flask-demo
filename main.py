from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():

    name= request.args.get("name")
    print(name)
    return name+"hello world"


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
