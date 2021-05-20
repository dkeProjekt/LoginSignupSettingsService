#!flask/bin/python
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from pymongo import MongoClient
from datetime import date

today = date.today()

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/signup', methods=['POST'])
def signup():
    if not request.json:
        abort(400)
    email = request.json.get("email")
    username = request.json.get("username")
    password = request.json.get("password")
    if signup(email, username, password):
        return jsonify({'signup_successful': True, 'username': username, 'password': password})
    else:
        return jsonify({'signup_successful': False, 'username': username, 'error': "Username already taken!"})


def signup(email, username, password):
    client = MongoClient(
        "mongodb+srv://Adri25:adri1234@cluster0.taxsc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client['PRDKE']
    collection = database['UserData']
    user = collection.find_one({"name": username})
    if user is not None:
        return False
    new_user = {"name": username, "password": password, "registration_date": str(date.today()), "email": email}
    collection.insert_one(new_user)
    return True


if __name__ == '__main__':
    app.run(debug=True, port=5002)
