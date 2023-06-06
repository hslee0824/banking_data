import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import io

with open('../test/simplified_model_gbm.pkl', 'rb') as f:
    model = pickle.load(f)

sample_test = pd.read_csv('sample_test.csv')

from flask import Flask, request, jsonify, render_template

test = pd.read_csv('sample_test.csv')

def cat_to_num(test):
    # HAVE TO PERFORM LABEL ENCODING MANUALLY

    print("Converted categorical data into numeric values")
    print("\n")
    return test

def drop_col(test):
    cols = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage',
    'GarageYrBlt', 'GarageCond', 'GarageType', 'GarageFinish', 'GarageQual',
    'BsmtFinType2', 'BsmtExposure', 'BsmtQual', 'BsmtCond', 'BsmtFinType1',
    'MasVnrArea', 'MasVnrType']
    test = test.drop(columns=cols)
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

    # # Convert user inputs into DataFrame form
    inputs_to_csv = pd.DataFrame(inputs, index=[0])
    print("Convert inputs into Dataframe format")
    print("Input:")
    print(inputs_to_csv.head())

    # Perform prediction
    result_cat_to_num = cat_to_num(inputs_to_csv)
    print("Performed conversion categorical values into numeric")
    print("After performing Label Encoding: ")
    print(result_cat_to_num.head())

    # Drop unnecessary columns
    result_drop_col = drop_col(result_cat_to_num)
    print("Drop unnecessary columns")

    # Save the user inputs
    result_drop_col.to_csv("test_cols.csv", index=False)

    result_pred = predict(result_drop_col)
    print("Successfully predicted value")
    print("Result: ", result_pred)

    return render_template("result.html", result_pred=result_pred)
if __name__ == "__main__":
    app.run(debug=True)
