"""Reddit prediction model Flask App"""

from flask import Flask, jsonify, render_template, request

import json
import pickle
import pandas as pd
import sklearn
from urllib.request import urlopen

    
app = Flask(__name__)
pickled = "https://github.com/chowell2000/bw_spotify5/raw/master/model_1.pkl"
pickled_scaler = "https://github.com/chowell2000/bw_spotify5/raw/master/scaler_1.pkl"
pickled_df = "https://github.com/chowell2000/bw_spotify5/raw/master/df.pkl"

model = pickle.load(urlopen(pickled))
scaler = pickle.load(urlopen(pickled_scaler))
lookup = pd.read_pickle(pickled_df)

cols = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence']

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/querytest", methods=['POST'])
def query_test():
    x = request.get_json(force=True)
    return x
    # render_template('predict.html', forum = x)


@app.route("/predict", methods=['POST'])
def predict(data=None):
    try:
        if request.method == 'POST':
            data = request.get_json(force=True)
    except KeyError:
        return ('''Bad request: value missing''')
    else:
        def model_prediction(data):
            data_df = pd.DataFrame(columns=cols)
            for i in range(len(data)):
                temp = pd.DataFrame.from_records(data[i], index=[i])
                data_df = data_df.append(temp[cols])

            data_scaled = pd.DataFrame(scaler.transform(data_df), columns=cols)
            
            
            predict = model.kneighbors(data_scaled, return_distance=False)

            # return predicter[0]
            return predict
        prediction = model_prediction(data)
        result = []
        for i in range(len(prediction[0])):
            resi = lookup[cols + ['track_id', 'track_name']].iloc[prediction[0][i]].to_dict()
            result.append(resi)
        return str(result)


@app.route("/about")
def preds():
    return render_template('about.html')
