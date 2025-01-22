from flask import Flask, request, jsonify
import flask
import json
from flask_cors import CORS
app = Flask(__name__)
stockList = [""]
@app.route("/")
def hello():
    return "hello World"


@app.route("/stock_update", methods=["PUT"])
def set_stocks():
    response = request.get_json()
    new_list = response.get("StockList")
    if not new_list:
        return jsonify({"error":"Missing proper updated stockList!!"}), 400
    stockList = new_list
    return jsonify({"success":"Stock list has been updated to size ${}"}), 200



if __name__ == "__main__":
    app.run("localhost", 6969)