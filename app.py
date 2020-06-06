from flask import Flask, request, abort

import sklearn
# from ie_nlp_utils.tokenization import tokenize as tk

import argparse
from platform import python_version

app = Flask(__name__)

@app.route("/")
def api_get_versions():
    """Sample endpoints with dynamic URLs"""
    # args = dict(request.args)
    return {
    "scikit-learn": sklearn.__version__,
    "Python": python_version(),
    }