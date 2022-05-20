
import tkinter as tk
from tkinter import BOTH
from tkinter.messagebox import showinfo

class ClientWindow():
    def __init__(self):        
        # configure the client window
        self.client = tk.Tk()
        self.client.title('Client Window')
        self.client.iconbitmap('icons/rat.ico')
        self.client.geometry('350x650+600+200')
        self.client.config(bg='black')
        self.client.resizable(0,0)

        # setting layout frames
        self.header_frame = tk.Frame(self.client, width=600, height=100, bg='black')
        self.midle_frame = tk.Frame(self.client, width=600, height=300, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.footer_frame = tk.Frame(self.client, width=600, height=50, bg='black')
        self.header_frame.pack()
        self.midle_frame.pack(padx = 25, pady= (20,25), fill=BOTH)
        self.footer_frame.pack()

        # header labels
        self.header_label_1 = tk.Label(self.header_frame, text='RAT', bg='black', fg='white', font=('helvetica', 25))
        self.rat_image = tk.PhotoImage(file='pictures/rat.png')
        self.header_label_2 = tk.Label(self.header_frame, image=self.rat_image, bg='black')
        self.header_label_1.grid(row=0, column=0, padx=20)
        self.header_label_2.grid(row=0, column=1, padx=20, ipadx=10, ipady=10)

        # midle labels and buttons
        self.midle_label_1 = tk.Label(self.midle_frame, text='Chat', bg='black', fg='white', font=('helvetica', 15))
        self.midle_label_1.pack(pady=10)
        self.midle_text = tk.Text(self.midle_frame, width=40, height=22, bg='black', fg='lightgreen', font=('helvetica',  10), insertbackground='lightgreen')
        self.midle_text.pack()
        self.midle_bottom_frame = tk.Frame(self.midle_frame, bg='black')
        self.midle_bottom_frame.pack()
        self.midle_bottom_info_button = tk.Button(self.midle_bottom_frame, width= 10, text='Info', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_bottom_info_button.grid(row=0, column=1, padx=10, pady=10)
        self.midle_bottom_exit_button = tk.Button(self.midle_bottom_frame, width= 10, text='Exit', bg='orange', fg='black', font=('helvetica', 15), command=self.client.destroy)
        self.midle_bottom_exit_button.grid(row=0, column=2, padx=10, pady=10)
        
        # footer label
        self.footer_label_1 = tk.Label(self.footer_frame, text='by Rat Masters', bg='black', fg='white', font=('helvetica', 10))
        self.footer_label_1.pack()
        
        # Welcome
        self.midle_text.insert("1.0", "Hello from Rat masters!\nWelcome!")

        self.client.mainloop()
 