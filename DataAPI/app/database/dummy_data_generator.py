import datetime
import json
import random
import pymongo

client = pymongo.MongoClient("mongodb://density:density@cluster0-shard-00-00-cvcng.gcp.mongodb.net:27017,cluster0-shard-00-01-cvcng.gcp.mongodb.net:27017,cluster0-shard-00-02-cvcng.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["density"]


def simulate_data():
    data = json.loads(open('F:\\Projects\\trackerapp\\DataAPI\\app\\database\\dummy.json').read())
    return data


def push_realtimedata():
    basetimestamp = datetime.datetime.now()
    for i in range(0,100):
        simulate_num_data(basetimestamp + datetime.timedelta(0, 0, 0, 0, i))


def simulate_num_data(date_time):
    nodeIds = [4, 5, 6, 7]
    for i in nodeIds:
        currentVolume = random.randint(50, 100)
        consumption = random.randint(50, currentVolume)
        slack = currentVolume - consumption
        slackPercent = slack / consumption * 100
        tag = get_tag(slackPercent)
        data = {
            "timeStamp": date_time,
            "currentVolume": currentVolume,
            "consumption": consumption,
            "slack": slack,
            "tag": tag
        }
        push_data_to_cloud(i, data)


def get_tag(slack_percent):
    if slack_percent < 5:
        return "L"
    elif slack_percent > 15:
        return "H"
    else:
        return "M"


def push_data_to_cloud(nodeId, data):
    forThis = {"nodeId": nodeId}
    doThis = {"$push": {"data": data}}
    db.nodeData.update(forThis, doThis)

