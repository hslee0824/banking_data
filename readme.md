## house price prediction
### link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview/evaluation
--------
### folder descriptions: 
#### "building_model" folder: All the necessary files for the buidling model
##### 1. model built by simplified_version.ipynb
##### 2. train, test and result files are stored in the "train_test_results_datasets" folder
##### 3. label encoding dictionary is encoding_mapping.txt
##### 4. encoding_mappaing, object_cols and model are stored in the "pkl_files" folder
##### 5. graphs are stroed in "graphs" folder
--------
#### "deploy" folder : All the necessary files for the deploying model
##### 1. "app.py" : load model and allow user to input values. 
##### 2. webpages are stored in the "templates" folder
--------
### Detail description for input:
#### The description of all the columns stored in "/building_model/train_test_results" folder
#### We restricted user inputs in the following form:
#### 1. MSSubClass: 120, 150, 160, 180, 190, 20, 30, 40, 45, 50, 60, 70, 75, 80, 85, 90
#### 2. MSZoning: 'C (all)', 'FV', 'RH', 'RL', 'RM'
#### 3. Street: Grvl, Pave
#### 4. LotShape: 'IR1', 'IR2', 'IR3', 'Reg'
#### 5. LandContour: 'Bnk', 'HLS', 'Low', 'Lvl'
#### 6. Utilities: 'AllPub', 'NoSeWa'
#### 7. LotConfig: 'Corner', 'CulDSac', 'FR2', 'FR3', 'Inside'
#### 8. LandSlope: 'Gtl', 'Mod', 'Sev'
#### 9. 'Neighborhood': Blmngtn', 'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr',
####                    'Crawfor': 6,
  'Edwards': 7,
  'Gilbert': 8,
  'IDOTRR': 9,
  'MeadowV': 10,
  'Mitchel': 11,
  'NAmes': 12,
  'NPkVill': 13,
  'NWAmes': 14,
  'NoRidge': 15,
  'NridgHt': 16,
  'OldTown': 17,
  'SWISU': 18,
  'Sawyer': 19,
  'SawyerW': 20,
  'Somerst': 21,
  'StoneBr': 22,
  'Timber': 23,
  'Veenker': 24},