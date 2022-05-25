import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import socket
import time

class Commands():
    def __init__(self, app):
        self.client = app.client
        self.client_addr = app.client_addr
        self.command = app.command
        self.ip = app.ip
        self.port = app.port
        self.s = app.s

    def clear_screen(self):
            os.system('cls')

    # def download(self, client, command):
    #     filename = command.split()[1]
    #     with open(filename, 'wb') as f:
    #         while True:
    #             bits = client.recv(1024)
    #             if b'DONE' in bits:
    #                 f.write(bits[:-4])
    #                 print('Transfer complete')
    #                 break
    #             elif b'File not found' in bits:
    #                 print('File not found')
    #                 break
    #             else:
    #                 f.write(bits)

    def send_data(self, s, output_data):
        size_of_data = str(len(output_data))
        self.s.send(bytes(size_of_data,'utf8'))
        time.sleep(2)
        s.send(output_data)
    
    def recv_data(self, s):
        original_size = s.recv(2048).decode('utf-8')
        original_size = int(original_size)
        data = s.recv(2048)
        while len(data) != original_size:
            data = data + s.recv(2048)
        return data

    def upload(self, s, output_data):
        s = self.s
        self.size_of_data = str(len(output_data))
        s.send(bytes(self.size_of_data,'utf8'))
        time.sleep(2)
        s.send(output_data)
 
    def download(self, s):
        s = self.s
        original_size = s.recv(2048)#.decode('utf-8')
        original_size = int(original_size)
        data = s.recv(2048)
        while len(data) != original_size:
            data = data + s.recv(2048)
        return data

    def button_clicked(self):
            print('Taking screenshot')
            self.client.send(b'screen')
            showinfo(title='Information', message='Screenshot taken!')

    def button2_clicked(self):
            print('Shuttingdown')
            self.client.send(b'shutdown /s')
            showinfo(title='Information', message='Remote has been shutdown!')
        
