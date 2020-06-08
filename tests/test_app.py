from flask import Flask
import sklearn
import ie_bike_model
from platform import python_version

import pytest
import os, sys
from werkzeug.exceptions import BadRequest

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import app as flaskapp


flaskapp.app.config["TESTING"] = True


def test_api_get_versions():
    with flaskapp.app.test_request_context("/"):
        assert isinstance(flaskapp.api_get_versions(), dict)
        assert set(flaskapp.api_get_versions().values()) == {
            sklearn.__version__,
            python_version(),
            ie_bike_model.__version__,
        }


def test_api_train_and_persist():
    with flaskapp.app.test_client() as tc:
        url = "/train_and_persist"
        response = tc.post(url, data={})
        assert isinstance(response.json, dict)
        assert isinstance(response.json["persisted-model-parameters"], dict)
        assert isinstance(response.json["out-of-bag-R2-score"], float)
        assert isinstance(response.json["top10-feature-importances"], list)


valid_endpoint = "/predict?date=2012-01-01T00:00:00&weathersit=1&temperature_C=9.84&feeling_temperature_C=14.395&humidity=81.0&windspeed=0"
wrong_endpoint = "/predict?date=2012-01-01T00:00:00&temperature=9.84&feeling_temperature=14.395&humidity=81.0&windspeed=0"


def test_api_predict():
    with flaskapp.app.test_request_context(valid_endpoint):
        assert isinstance(flaskapp.api_predict(), dict)
        assert isinstance(flaskapp.api_predict().get("result"), int)
        assert isinstance(flaskapp.api_predict().get("elapsed_time"), float)

    with flaskapp.app.test_request_context(wrong_endpoint):
        with pytest.raises(Exception):
            assert isinstance(Exception, BadRequest)
