import requests
import shutil
import subprocess

print("start download latest")
url = 'http://lerts91.fvds.ru/api/latest'
response = requests.get(url, stream=True)
with open('/home/swpi/growOrange/latest/latest.ino', 'wba+') as out_file:
    shutil.copyfileobj(response.raw, out_file)
    print('End download\r\nstart upload')
del response



