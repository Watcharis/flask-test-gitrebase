from flask import Flask, jsonify, request

def hello():
    s = "hello world"
    return jsonify({"message": s}), 200