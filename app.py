import random
import os

from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def random_generator_api():
    data = random.randint(1, 1000)
    return make_response(str(data), 200)


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
