#!flask/bin/python
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/get_test', methods=['GET'])
def get_test():
    return "hallo get"


@app.route('/post_test', methods=['POST'])
def post_test():
    return "hallo post"


@app.route('/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    username = request.json.get("username")
    password = request.json.get("password")

    client = MongoClient(
        "mongodb+srv://Adri25:adri1234@cluster0.taxsc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client['PRDKE']
    collection = database['UserData']
    user = collection.find_one({"name": username})
    if user is None or user["password"] != password:
        return jsonify({'login_successful': False, 'username': username, 'error': "Invalid username or password!"})
    else:
        return jsonify({'login_successful': True, 'username': username, 'id': user['follow_id']})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
