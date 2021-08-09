from flask import Flask, jsonify, request

def hello():
    return jsonify({"message": "hello world"}), 200