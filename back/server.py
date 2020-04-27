from flask import Flask, render_template, Response, jsonify, request, send_from_directory
import pathlib
from os import path
from flask_cors import CORS

from request import Request
from jsonparser import JsonParser
from database import DataBase


app = Flask(__name__, template_folder='../front')
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('../front', filename)

    
@app.route('/get', methods=['GET', 'POST'])
def get():
    # print(request.args)
    region = request.args.get('r_region')
    case = request.args.get('r_case')
    benefit = request.args.get('r_benefit')
    number = request.args.get('r_number')
    location = request.args.get('r_location')
    token = request.args.get('r_token')
    # print('*****', token)
    req = Request()
    req.create_request(region, benefit, case, number, location)
    req.send_request()
    jp = JsonParser(req.rec_response())
    jp.parse(token)
    status_code = Response(status=200)
    # print(jp.response)
    return jsonify(jp.response)

@app.route('/displayfav', methods=['GET', 'POST'])
def displayfav():
    token = request.args.get('tokenId')
    req = Request()
    db = DataBase()
    id_list = db.get_fav_id(token)
    response_dict = []
    for id in id_list:
        req.create_fav_request(id)
        req.send_request()
        jp = JsonParser(req.rec_response())
        jp.parse_id_response()
        response_dict.extend(jp.response)
    return jsonify(response_dict)

@app.route('/signin', methods=['GET'])
def sign_in():
    login = request.args.get('login')
    password = request.args.get('password')
    db = DataBase()
    # print(login, password)
   
    return jsonify([{
        "ticket": str(db.check_user(login, password))}
    ])


@app.route('/signup', methods=['GET'])
def sign_up():
    login = request.args.get('login')
    password = request.args.get('password')
    db = DataBase()
    # print(login, password)
   
    return jsonify([{
        "ticket": str(db.add_user(login, password))}
    ])
   

@app.route('/addfav', methods=['POST', 'GET'])
def add_fav():
     token = request.args.get('tokenId')
     id = request.args.get('queueId')
     # print(token, id)
     db = DataBase()
     db.add_to_fav(token, id)
     return "ok", 200


@app.route('/removefav', methods=['POST', 'GET'])
def remove_fav():
     token = request.args.get('tokenId')
     id = request.args.get('queueId')
     # print(token, id)
     db = DataBase()
     db.remove_fav(token, id)
     return "ok", 200


if __name__ == '__main__':
    app.run(port=8080)
