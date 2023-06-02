import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import io

with open('../test/model.pkl', 'rb') as f:
    model = pickle.load(f)

sample_test = pd.read_csv('sample_test.csv')
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
    # Get user input from index.html
    inputs={}
    for col in sample_test.columns:
        if col == 'Id':
            continue
        else:
            input = request.form.get(col)
            inputs.update({col:input})
    print("Loaded all the inputs")

    # Convert user inputs into DataFrame form
    inputs_to_csv = pd.DataFrame(inputs, index=[0])
    print("Convert inputs into Dataframe format")

    # Save the user inputs
    inputs_to_csv.to_csv("test_cols.csv", index=False)
    print("Saved inputs to csv file")

    # Perform prediction
    result_cat_to_num = cat_to_num(inputs_to_csv)
    print("Performed conversion categorical values into numeric")

    result_pred = predict(result_cat_to_num)
    print("Successfully predicted value")
    print("Result: ", result_pred)
    
    return render_template("result.html", result_pred=result_pred)
if __name__ == "__main__":
    app.run(debug=True)
