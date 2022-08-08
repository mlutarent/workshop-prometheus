import os

from flask import Flask

app = Flask(__name__)

counter = 0

service_name = os.getenv('SERVICE_NAME')


@app.route('/metrics')
def metrics():
    global counter
    counter += 1
    data = f'http_requests_total{{instance="{service_name}", job="{service_name}", method="GET", status_code="200"}} {counter}'
    return data, 200
