from flask import Flask
from flask import request

from PIL import Image
import os

app = Flask(__name__)


@app.route('/training-set', methods=['POST'])
def hello_world():
    incoming_data = request.get_json()

    path = r"{}".format(incoming_data['path'])

    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            im = Image.open(f)
            im.show()

    return path


if __name__ == '__main__':
    app.run()
