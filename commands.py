import os
from tkinter import ttk
from tkinter.messagebox import showinfo

class Commands():
    def __init__(self):
        pass


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
            showinfo(title='Information', message='Hello, Tkinter!')
        
