from flask import Flask,request,abort
import argparse
import sklearn
from ie_nlp_utils.tokenization import tokenize as tk

app = Flask(__name__)

