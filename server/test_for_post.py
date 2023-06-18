import requests

# Define the URL of the server
url = 'https://house-price-prediction-1e0q.onrender.com/'  # Replace with the actual server URL

# Define the data to send
data = {
    'key1': 'value1',
    'key2': 'value2',
    # Add more key-value pairs as needed
}

# Send the POST request
response = requests.post(url, data=data)

# Check the response status code
if response.status_code == 200:
    print('Request successful')
else:
    print(f'Request failed with status code: {response.status_code}')
