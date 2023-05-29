import requests

resp = requests.post("http://127.0.0.1:5000", files={'file' : open('sample_test.csv', 'rb')})

print(resp.json())

