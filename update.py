import requests
import shutil

print("start download latest")
url = 'http://lerts91.fvds.ru/api/latest'
response = requests.get(url, stream=True)
with open('latest/latest.ino', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
#    print('End download')
del response



