from flask import Flask, request
from flask_cors import CORS, cross_origin
from app.database.database_service import get_data
from app.forecast_service import forecast_future
import pymongo

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
    # future_data = forecast_future(data)
    # return future_data.__str__()

@app.route('/<node_id>')
@cross_origin()
def forecastnode(node_id):
    names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
    company_type = ['LLC','Inc','Company','Corporation']
    client = pymongo.MongoClient("mongodb://density:density@cluster0-shard-00-00-cvcng.gcp.mongodb.net:27017,cluster0-shard-00-01-cvcng.gcp.mongodb.net:27017,cluster0-shard-00-02-cvcng.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.density
    print(db);
    node={
        "name": names,
        "company": company_type
    }
    # db.nodeData.insert_one(node)
    # print(db);
    ls=db.nodeData.find({'name':'Kitchen'})
    print(ls.count());
    return 'Hello, World!';
