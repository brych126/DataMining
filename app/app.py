from flask import Flask, request, jsonify, render_template
from sklearn.linear_model import LinearRegression
from collections import namedtuple
import pandas as pd
import os
import pickle
import json

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources/movies_cleaned.csv")

data = pd.read_csv(RESOURCE_DIR)

X = data[['budget', 'runtime', 'gross']]
Y = data['score']

regr = LinearRegression()
regr.fit(X, Y)

pickle.dump(regr, open('model.pkl','wb'))
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

def convert(dto):
    return namedtuple('movie', dto.keys())(*dto.values())

@app.route('/')
def home():
    return str("Api is alive")

@app.route('/predict', methods=['POST'])
def resPost():
    movieObj = json.loads(request.data, object_hook=convert)

    arr = list(zip([movieObj.budget], [movieObj.runtime], [movieObj.gross]))
    print(arr)

    prediction = model.predict(arr)
    formatted_string = "{:.4f}".format(prediction[0])
    print({'predicted movie score': prediction[0]})

    return jsonify({'predicted movie score': formatted_string})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)