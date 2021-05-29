#!flask/bin/python
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from pymongo import MongoClient
from datetime import date
import json

today = date.today()

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/get_all_users', methods=['GET'])
def get_all_users():
    client = MongoClient(
        "mongodb+srv://Adri25:adri1234@cluster0.taxsc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client['PRDKE']
    collection = database['UserData']
    users = collection.find()
    user_names = []
    for user in users:
        user_names.append(user["name"])

    user_names_json = json.dumps(user_names)
    return jsonify({'get_all_users_successful': True, "list_of_users": user_names_json})


if __name__ == '__main__':
    app.run(debug=True, port=5004)