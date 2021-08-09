from flask import Flask, jsonify, request

def echo():
    return jsonify({"message": "echo world"}), 200

def miss():
    return jsonify({"message": "mono mise"}), 200