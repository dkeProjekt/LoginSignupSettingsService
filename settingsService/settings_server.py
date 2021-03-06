#!flask/bin/python
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from pymongo import MongoClient
from datetime import date

today = date.today()

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/get_personal_data', methods=['POST'])
def get_personal_data():
    if not request.json:
        abort(400)
    username = request.json.get("username")

    client = MongoClient("localhost", 27017)
    database = client['PRDKE']
    collection = database['UserData']
    user = collection.find_one({"name": username})
    if user is None:
        return jsonify({'get_data_successful': False, 'username': username, 'email': '', 'registration_date': '', 'error': "Something went wrong!"})
    return jsonify({'get_data_successful': True, 'username': username, 'email': user["email"], 'registration_date': user['registration_date'], 'error': ''})


@app.route('/change_password', methods=['POST'])
def change_password():
    if not request.json:
        abort(400)
    username = request.json.get("username")
    password_old = request.json.get("password_old")
    password_new = request.json.get("password_new")
    success, error = change_password(username, password_old, password_new)
    if success:
        return jsonify({'change_password_successful': True, 'username': username, 'error': ''})
    else:
        return jsonify({'change_password_successful': False, 'username': username, 'error': error})


def change_password(username, password_old, password_new):
    client = MongoClient("localhost", 27017)
    database = client['PRDKE']
    collection = database['UserData']
    user = collection.find_one({"name": username})
    if user is None:
        return False, "Something went wrong."
    if user["password"] != password_old:
        return False, "Old password incorrect!"
    query = {"name": username}
    new_value = {"$set": {"password": password_new}}
    collection.update_one(query, new_value)
    return True, None


if __name__ == '__main__':
    app.run(debug=True, port=5003)
