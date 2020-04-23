from flask import Flask, render_template, Response, jsonify, request
import pathlib
from os import path
from flask_cors import CORS

from request import Request
from jsonparser import JsonParser


app = Flask(__name__, template_folder='../front')
CORS(app)

@app.route('/get', methods=['GET', 'POST'])
def index():
    print(request.args)
    region = request.args.get('r_region')
    case = request.args.get('r_case')
    benefit = request.args.get('r_benefit')
    req = Request()
    req.create_request(region, benefit, case)
    req.send_request()
    jp = JsonParser(req.rec_response())
    jp.parse()
    status_code = Response(status=200)
    print(jp.response)
    return jsonify(jp.response)

if __name__ == '__main__':
    app.run(port=8080)
