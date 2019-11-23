from flask import Flask, request
from flask_cors import CORS, cross_origin
from app.database.database_service import get_data
from app.forecast_service import forecast_future

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')


@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'


@app.route('/forecast/<node_id>')
@cross_origin()
def forecast(node_id):
    data = get_data(node_id)
    future_data = forecast_future(data)
    return future_data.__str__()
