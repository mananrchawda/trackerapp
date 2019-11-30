from flask import Flask, request
from flask_cors import CORS, cross_origin
from app.database.dummy_data_generator import simulate_data, push_realtimedata
from app.database.database_service import push_data_to_cloud

app = Flask(__name__)
CORS(app)


@app.route('/push-data')
@cross_origin()
def push_data():
    #data = simulate_data()
    #push_data_to_cloud(data)
    push_realtimedata()
    return 'Hello'


@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'
