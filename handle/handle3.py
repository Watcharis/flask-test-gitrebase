from flask import Flask, jsonify, request

def writeEcho():
    return jsonify({"message": "write echo"}), 200