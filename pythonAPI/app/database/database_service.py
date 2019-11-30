from app.database import constants
import requests


def get_data(node_id):
    # API call to database service
    node_data_access_url = constants.NODE_URL + '/' + node_id
    # request_data = requests.get(node_data_access_url)

    data = []
    for i in range(1, 10):
        data.append(i * int(node_id))
    return data


