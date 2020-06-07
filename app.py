from flask import Flask, request, abort, jsonify
import sklearn
import ie_bike_model
from ie_bike_model.model import train_and_persist, predict
import argparse
from platform import python_version
import datetime as dt
import time


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
def api_get_versions():
    """Basic endpoint displaying relevant versions"""
    return {
        "scikit-learn": sklearn.__version__,
        "ie-bike-model": ie_bike_model.__version__,
        "Python": python_version(),
    }


@app.route("/train_and_persist")
def api_train_and_persist():
    """Endpoint to train and persist the model defined in lib/"""
    regressor, score, top10_features = train_and_persist(compression_factor=True)

    return {"status": "ok", "persisted-model-parameters": regressor.get_params(), "out-of-bag-R2-score": score, "top10-feature-importances": top10_features}


@app.route("/predict")
def api_predict():
    """Endpoint to retrieve model predictions from URL parameters"""
    start_time = time.time()
    args = dict(request.args)

    try:
        args["date"] = dt.datetime.strptime(args["date"], "%Y-%m-%dT%H:%M:%S")
        args["weathersit"] = int(args["weathersit"])
        args["temperature_C"] = float(args["temperature_C"])
        args["feeling_temperature_C"] = float(args["feeling_temperature_C"])
        args["humidity"] = float(args["humidity"])
        args["windspeed"] = float(args["windspeed"])

    except:
        abort(
            400,
            description="400: Missing/incorrect URL parameters.\n\nMake sure these are passed as:\n\n?date\n&weathersit\n&temperature_C\n&feeling_temperature_C\n&humidity\n&windspeed",
        )

    return {"result": predict(args), "elapsed_time": round(time.time() - start_time, 3)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Flask application to deploy ie-bike-model"
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    app.run(debug=args.debug)
