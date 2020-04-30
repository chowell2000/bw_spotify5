"""Reddit prediction model Flask App"""

from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/querytest", methods=['GET'])
def query_test():
    x = request.args.get("text")
    return render_template('predict.html', forum = x)



@app.route("/predict", methods=['GET', 'POST'] )
def predict():
    # text = 'I want to play the new call of duty'
    text = request.args.get("text")
    # nn = pickle.load(open('model.pkl', 'rb'))
    # vect = pickle.load(open('countvectorizer.pkl', 'rb'))
    # subset = pd.read_pickle("./dataset.pkl")
    # new = vect.transform([text])
    
    # x = nn.kneighbors(new.todense())
    
    # y = x[1][0][0]
    # z = subset.iloc[y][0]
    
    return render_template('predict.html', forum=z)



@app.route("/about")
def preds():
    return render_template('about.html')

# ,method = POST