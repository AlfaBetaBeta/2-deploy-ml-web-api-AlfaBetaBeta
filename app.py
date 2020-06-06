from flask import Flask, request, abort

import sklearn
import ie_bike_model
from ie_bike_model.model import train_and_persist

import argparse
from platform import python_version

app = Flask(__name__)

@app.route("/")
def api_get_versions():
    """Basic endpoint displaying relevant versions"""
    return {
    "scikit-learn": sklearn.__version__,
    "ie-bike-model": ie_bike_model.__version__,
    "Python": python_version(),
    }




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Flask application to deploy ie-bike-model")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    app.run(debug=args.debug)