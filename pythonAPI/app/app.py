from flask import Flask, request
from flask_cors import CORS, cross_origin
from app.database.database_helper import get_data


app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')


@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'


@app.route('/forecast')
@cross_origin()
def forecast():
    node_id = request.args.get('nodeId')
    data = get_data(node_id)
    return data.__str__()
