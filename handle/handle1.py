from flask import Flask, jsonify, request

def hello():
    s = "hello world"
    return jsonify({"message": s}), 200


def voice():
    s = "blavlallva"
    return jsonify({"message": s}), 200