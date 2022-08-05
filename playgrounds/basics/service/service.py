from flask import Flask

app = Flask(__name__)

counter = 0


@app.route('/metrics')
def metrics():
    global counter
    counter += 1
    data = f'http_requests_total{{instance="service-01", job="service-a", method="GET", status_code="200"}} {counter}'
    return data, 200
