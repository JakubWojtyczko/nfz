from flask import Flask, render_template, Response, jsonify, request
import pathlib
from os import path
from flask_cors import CORS

from request import Request
from jsonparser import JsonParser
from database import DataBase


app = Flask(__name__, template_folder='../front')
CORS(app)

@app.route('/get', methods=['GET', 'POST'])
def index():
    # print(request.args)
    region = request.args.get('r_region')
    case = request.args.get('r_case')
    benefit = request.args.get('r_benefit')
    number = request.args.get('r_number')
    location = request.args.get('r_location')
    req = Request()
    req.create_request(region, benefit, case, number, location)
    req.send_request()
    jp = JsonParser(req.rec_response())
    jp.parse()
    status_code = Response(status=200)
    # print(jp.response)
    return jsonify(jp.response)

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
   
   
    
if __name__ == '__main__':
    app.run(port=8080)
