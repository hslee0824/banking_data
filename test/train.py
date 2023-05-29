# import libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import numpy as np
from sklearn.model_selection import train_test_split
import pickle

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train_ID = train['Id']
test_ID = test['Id']

def replace_null_values():
    # ----Replace all null values in train and test datasets ----# 

    # LotFrontage
    train['LotFrontage'] = train['LotFrontage'].fillna(train['LotFrontage'].median())
    test['LotFrontage'] = test['LotFrontage'].fillna(test['LotFrontage'].median())

    # Alley
    train['Alley'] = train['Alley'].fillna("None")
    test['Alley'] = test['Alley'].fillna("None")

    # MasVnrType, MasVnrArea
    train['MasVnrType'] = train['MasVnrType'].fillna("None")
    train['MasVnrArea'] = train['MasVnrArea'].fillna(0.0)
    test['MasVnrType'] = test['MasVnrType'].fillna("None")
    test['MasVnrArea'] = test['MasVnrArea'].fillna(0.0)

    # BsmtExposure
    train.loc[train['BsmtExposure'].isnull() & train['BsmtCond'].notnull(), 'BsmtExposure'] = 'Av'
    test.loc[test['BsmtExposure'].isnull() & test['BsmtCond'].notnull(), 'BsmtExposure'] = 'Av'

    # BsmtFinType2
    train.loc[train['BsmtFinType2'].isnull() & train['BsmtFinType1'].notnull(), ['BsmtFinType1']] = "None"
    test.loc[test['BsmtFinType2'].isnull() & test['BsmtFinType1'].notnull(), ['BsmtFinType1']] = "None"

    # BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinType2
    train['BsmtQual'] = train['BsmtQual'].fillna("None")
    train['BsmtCond'] = train['BsmtCond'].fillna("None")
    train['BsmtExposure'] = train['BsmtExposure'].fillna("None")
    train['BsmtFinType1'] = train['BsmtFinType1'].fillna("None")
    train['BsmtFinType2'] = train['BsmtFinType2'].fillna("None")
    test['BsmtQual'] = test['BsmtQual'].fillna("None")
    test['BsmtCond'] = test['BsmtCond'].fillna("None")
    test['BsmtExposure'] = test['BsmtExposure'].fillna("None")
    test['BsmtFinType1'] = test['BsmtFinType1'].fillna("None")
    test['BsmtFinType2'] = test['BsmtFinType2'].fillna("None")

    # Electrical
    train['Electrical'] = train['Electrical'].fillna("SBrkr")
    test['Electrical'] = test['Electrical'].fillna("SBrkr")

    # FireplaceQu
    train['FireplaceQu'] = train['FireplaceQu'].fillna("None")
    test['FireplaceQu'] = test['FireplaceQu'].fillna("None")

    # GarageType, GarageYrBlt, GarageFinish, GarageQual, GarageCond
    train['GarageType'] = train['GarageType'].fillna("None")
    train['GarageYrBlt'] = train['GarageYrBlt'].fillna(-1)
    train['GarageFinish'] = train['GarageFinish'].fillna("None")
    train['GarageQual'] = train['GarageQual'].fillna("None")
    train['GarageCond'] = train['GarageCond'].fillna("None")
    test['GarageType'] = test['GarageType'].fillna("None")
    test['GarageYrBlt'] = test['GarageYrBlt'].fillna(-1)
    test['GarageFinish'] = test['GarageFinish'].fillna("None")
    test['GarageQual'] = test['GarageQual'].fillna("None")
    test['GarageCond'] = test['GarageCond'].fillna("None")

    # PoolQC
    train['PoolQC'] = train['PoolQC'].fillna("None")
    test['PoolQC'] = test['PoolQC'].fillna("None")

    # Fence
    train['Fence'] = train['Fence'].fillna("None")
    test['Fence'] = test['Fence'].fillna("None")

    # MiscFeature
    train['MiscFeature'] = train['MiscFeature'].fillna("None")
    test['MiscFeature'] = test['MiscFeature'].fillna("None")


    # BsmtFinSF2, BsmtFinSF1, BsmtUnfSF, TotalBsmtSF, BsmtFullBath, BsmtHalfBath 
    # These attributes were not shown in train dataset EDA
    test['BsmtFinSF2'] = test['BsmtFinSF2'].fillna("None")
    test['BsmtFinSF1'] = test['BsmtFinSF1'].fillna(0.0)
    test['BsmtUnfSF'] = test['BsmtUnfSF'].fillna(0.0)
    test['TotalBsmtSF'] = test['TotalBsmtSF'].fillna(0.0)
    test['BsmtFullBath'] = test['BsmtFullBath'].fillna(0.0)
    test['BsmtHalfBath'] = test['BsmtHalfBath'].fillna(0.0)

    # MSZoning
    test['MSZoning'] = test['MSZoning'].fillna("RL")

    # Utilities
    test['Utilities'] = test['Utilities'].fillna("AllPub")

    # Exterior1st, Exterior2nd
    test['Exterior1st'] = test['Exterior1st'].fillna("VinylSd")
    test['Exterior2nd'] = test['Exterior2nd'].fillna("VinylSd")

    # KitchenQual
    test['KitchenQual'] = test['KitchenQual'].fillna("TA")

    # Functional
    test['Functional'] = test['Functional'].fillna("Typ")

    # GarageCars, GarageArea
    test['GarageCars'] = test['GarageCars'].fillna(0)
    test['GarageArea'] = test['GarageArea'].fillna(0.0)

    # SaleType
    test['SaleType'] = test['SaleType'].fillna("WD")
    print("Null values in train: ", train.isnull().sum().any())
    print("Null values in test: ", test.isnull().sum().any())
    print("\n")

def drop_ID():
    # Drop ID for both train and test datasets.
    train.drop(columns='Id', inplace=True)
    test.drop(columns='Id', inplace=True)
    print("Dropped ID in train and test")
    print("\n")

def cat_to_num():
    # MSSubClass are treat as categorical values
    train['MSSubClass'] = train['MSSubClass'].apply(str)

    # Year and month sold are transformed into categorical features.
    train['YrSold'] = train['YrSold'].astype(str)
    train['MoSold'] = train['MoSold'].astype(str)

    # MSSubClass are treat as categorical values
    test['MSSubClass'] = test['MSSubClass'].apply(str)

    # Year and month sold are transformed into categorical features.
    test['YrSold'] = test['YrSold'].astype(str)
    test['MoSold'] = test['MoSold'].astype(str)

    # train label encoding
    cols = list(train.select_dtypes(include='object').columns)
    for c in cols:
        lbl = LabelEncoder()
        lbl.fit(list(train[c].values))
        train[c] = lbl.transform(list(train[c].values))

    # test label encoding
    cols = list(test.select_dtypes(include='object').columns)
    for c in cols:
        lbl = LabelEncoder()
        lbl.fit(list(test[c].values))
        test[c] = lbl.transform(list(test[c].values))

    print("Converted categorical data into numeric values")
    print("\n")


def train_and_save_model():
    # split train datasets into feature X and target y
    X = train.drop(columns='SalePrice')
    y = train['SalePrice']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # perform feature importance

    model = LGBMRegressor(
        boosting_type='gbdt',
        num_leaves=31,
        learning_rate=0.1,
        n_estimators=100,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_alpha=0.1,
        reg_lambda=0.1,
        objective='regression'
    )
    model.fit(X_train, y_train)

    # save the model to disk
    pickle.dump(model, open("model.pkl", 'wb'))
    print("Saved model as model.pkl")
    print("\n")


replace_null_values()
drop_ID()
cat_to_num()
train_and_save_model()


