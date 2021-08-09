from flask import Flask, json, jsonify, request
from handle import handle1



app =Flask(__name__)



@app.route("/", methods=["GET"])
def getHello():
    return handle1.hello()





if __name__ == "__main__":
    app.run(host="localhost", port=5006)
