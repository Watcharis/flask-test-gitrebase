from flask import Flask, json, jsonify, request
from handle import handle1, handle2, handle3

app =Flask(__name__)

@app.route("/", methods=["GET"])
def getHello():
    return handle1.hello()

@app.route("/test", methods=["GET"])
def getEcho():
    return handle2.echo()

@app.route("/apply", methods=["GET"])
def getMiss():
    return handle2.miss()

@app.route("/echo", methods=["GET"])
def getWriteEcho():
    return handle3.writeEcho()

if __name__ == "__main__":
    app.run(host="localhost", port=5005)
