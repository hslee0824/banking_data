import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import io

with open('../test/model.pkl', 'rb') as f:
    model = pickle.load(f)

from flask import Flask, request, jsonify, render_template

def cat_to_num(test):
    # MSSubClass are treat as categorical values
    test['MSSubClass'] = test['MSSubClass'].apply(str)

    # Year and month sold are transformed into categorical features.
    test['YrSold'] = test['YrSold'].astype(str)
    test['MoSold'] = test['MoSold'].astype(str)

    # test label encoding
    cols = list(test.select_dtypes(include='object').columns)
    for c in cols:
        lbl = LabelEncoder()
        lbl.fit(list(test[c].values))
        test[c] = lbl.transform(list(test[c].values))

    print("Converted categorical data into numeric values")
    print("\n")
    return test

def drop_ID(test):
    # Drop ID for both train and test datasets.
    test.drop(columns='Id', inplace=True)
    print("Dropped ID in train and test")
    print("\n")
    return test

def predict(x):
    predictions = model.predict(x)
    return predictions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    input1 = request.form.get("input1")
    input2 = request.form.get("input2")
    input3 = request.form.get("input3")
    
    inputs = [input1, input2, input3]
    
    # Process the input values as needed
    
    return render_template("result.html", inputs=inputs)
if __name__ == "__main__":
    app.run(debug=True)
