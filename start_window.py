
import tkinter as tk
from tkinter import ttk, BOTH
from tkinter.messagebox import showinfo

class StartWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # configure the root window
        self.title('Start Window')
        self.iconbitmap('icons/rat.ico')
        self.geometry('600x500+500+200')
        self.config(bg='black')
        self.resizable(0,0)

        # setting layout frames
        self.header_frame = tk.Frame(self, width=600, height=100, bg='black')
        self.midle_frame = tk.Frame(self, width=600, height=350, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.footer_frame = tk.Frame(self, width=600, height=50, bg='black')
        self.header_frame.pack()
        self.midle_frame.pack(padx = 25, pady= (20,25), fill=BOTH)
        self.footer_frame.pack()

        # header labels
        self.header_label_1 = tk.Label(self.header_frame, text='Remote Administration Tool', bg='black', fg='white', font=('helvetica', 25))
        self.rat_image = tk.PhotoImage(file='pictures/rat.png')
        self.header_label_2 = tk.Label(self.header_frame, image=self.rat_image, bg='black')
        self.header_label_1.grid(row=0, column=0, padx=20)
        self.header_label_2.grid(row=0, column=1, padx=20, ipadx=10, ipady=10)

        # midle labels and buttons
        self.midle_label_1 = tk.Label(self.midle_frame, text='Run as:', bg='black', fg='white', font=('helvetica', 15))
        self.midle_label_1.pack(pady=10)
        self.midle_button_client = tk.Button(self.midle_frame, text='Client', fg='black', bg='lightgreen', font=('helvetica', 15))
        self.midle_button_client.pack(pady=10)
        self.midle_label_2 = tk.Label(self.midle_frame, text='or', bg='black', fg='white', font=('helvetica', 15))
        self.midle_label_2.pack(pady=10)
        self.midle_button_admin = tk.Button(self.midle_frame, text='Admin', fg='black', bg='orange', font=('helvetica', 15))
        self.midle_button_admin.pack(pady=10)
        self.midle_label_3 = tk.Label(self.midle_frame, text='If running as admin, please enter password:', bg='black', fg='white', font=('helvetica', 15))
        self.midle_label_3.pack(pady=10)
        self.midle_entry = tk.Entry(self.midle_frame, bg='black', fg='lightgreen', font=('helvetica', 15), justify='center', insertbackground='lightgreen')
        self.midle_entry.pack(pady=10)

        # footer label
        self.footer_label_1 = tk.Label(self.footer_frame, text='by Rat Masters', bg='black', fg='white', font=('helvetica', 10))
        self.footer_label_1.pack()
        

if __name__ == "__main__":
    app = StartWindow() 
    app.mainloop()

 