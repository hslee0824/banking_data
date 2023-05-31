import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import io

with open('test/model.pkl', 'rb') as f:
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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("index.html")
        file = request.files.get("file")
        if file is None or file.filename == "":
            return jsonify({"error" : "no file"})

        try:
            test = pd.read_csv(io.StringIO(file.stream.read().decode("UTF8")))
            num_test = cat_to_num(test)
            drop_Id_test = drop_ID(test)
            prediction = predict(test)
            data = {"Prediction" : prediction.tolist()}
            return jsonify(data)

        except Exception as e:
            return jsonify({"error" : str(e)})
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True)
