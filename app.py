from flask import Flask, request, abort

import sklearn
import ie_bike_model
from ie_bike_model.model import train_and_persist

import argparse
from platform import python_version

app = Flask(__name__)

@app.route("/")
def api_get_versions():
    """Sample endpoints with dynamic URLs"""
    # args = dict(request.args)
    return {
    "scikit-learn": sklearn.__version__,
    "ie-bike-model": ie_bike_model.__version__,
    "Python": python_version(),
    }