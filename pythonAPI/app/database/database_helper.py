from flask import current_app as app


def get_data(node_id):
    database_url = app.config['DATABASE_URL']
    data = []
    for i in range(1, 10):
        data.append(i * int(node_id))
    return data

