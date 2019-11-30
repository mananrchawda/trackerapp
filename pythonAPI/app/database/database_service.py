from app.database import constants
import requests
import pymongo


def get_data(node_id):
    # API call to database service
    # node_data_access_url = constants.NODE_URL + '/' + node_id

    client = pymongo.MongoClient("mongodb+srv://density:density@cluster0-cvcng.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test


    # request_data = requests.get(node_data_access_url)
    #
    # data = []
    # for i in range(1, 10):
    #     data.append(i * int(node_id))
    # return data


