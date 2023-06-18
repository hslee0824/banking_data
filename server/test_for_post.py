import requests

# Define the URL of the server
url = 'http://127.0.0.1:5000/process'  # Replace with the actual server URL

# Define the data to send
data = {
    'OverallQual': '10',
    'GrLivArea': '100',
    'TotalBsmtSF' : '100',
    'BsmtFinSF1' : '100',
    '1stFlrSF' : '100', 
    '2ndFlrSF' : '100',
    'GarageArea' : '100', 
    'LotArea' : '100', 
    'YearBuilt' : '2020',
    'GarageCars' : '3',
    'TotRmsAbvGrd' : '3'
    # Add more key-value pairs as needed
}

# Send the POST request
response = requests.post(url, data=data)

# Check the response status code
if response.status_code == 200:
    print('Request successful')
else:
    print(f'Request failed with status code: {response.status_code}')
