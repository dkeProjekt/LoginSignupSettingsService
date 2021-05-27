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
    follow_id = request.json.get("id")

    client = MongoClient(
        "mongodb+srv://Adri25:adri1234@cluster0.taxsc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client['PRDKE']
    collection = database['UserData']
    user = collection.find_one({"name": username})
    if user is not None:
        return jsonify({'signup_successful': False, 'username': username, 'error': "Username already taken!"})
    else:
        new_user = {"name": username, "password": password, "email": email, "follow_id": follow_id, "registration_date": str(date.today())}
        collection.insert_one(new_user)
    return jsonify({'signup_successful': True, 'username': username, 'id': follow_id})


if __name__ == '__main__':
    app.run(debug=True, port=5002)
