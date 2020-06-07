# Bike sharing prediction model

## Usage

```
$ pip install lib/
$ python app.py
$ python app.py -d
OR
$ python app.py --debug # To run the app in debug mode
```

Then open [this sample link](http://127.0.0.1:5000/predict?date=2012-01-01T00:00:00&weathersit=1&temperature_C=9.84&feeling_temperature_C=14.395&humidity=81.0&windspeed=0)
in your browser to check the endpoint `/predict`, [this link](http://127.0.0.1:5000/train_and_persist) to check the endpoint `/train_and_persist` or [this link](http://127.0.0.1:5000/) to check the endpoint `/`.

## Testing

```
$ cd tests
$ pytest -v
```