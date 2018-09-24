import requests
import shutil

url = 'http://127.0.0.1:5000/api/latest'
response = requests.get(url, stream=True)
with open('latest.ino', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

print("download PO")

