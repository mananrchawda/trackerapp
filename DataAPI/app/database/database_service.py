import pymongo
import jsonify


def push_data_to_cloud(data):
    client = pymongo.MongoClient("mongodb://density:density@cluster0-shard-00-00-cvcng.gcp.mongodb.net:27017,cluster0-shard-00-01-cvcng.gcp.mongodb.net:27017,cluster0-shard-00-02-cvcng.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client["density"]
    myquery = {"nodeId": 1}
    # newvalues = {"$set": {"data": [{"tag": "M"}]}}
    newvalues = {"$push": {"data": [{"tag": "L"}]}}
    # db.nodeData["data"]
    db.nodeData.update(myquery, newvalues)
    return ""
    #db.nodeData.insertMany(str(data["nodeData"]))
