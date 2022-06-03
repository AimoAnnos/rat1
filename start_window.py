import tkinter as tk
from tkinter import BOTH, END
from tkinter.messagebox import showinfo
import subprocess

class StartWindow():
    def __init__(self):
          
        # configure the start window
        self.start = tk.Tk()
        self.start.title('Start Window')
        self.start.iconbitmap('icons/rat.ico')
        self.start.geometry('600x500+500+200')
        self.start.config(bg='black')
        self.start.resizable(0,0)

        # setting layout frames
        self.header_frame = tk.Frame(self.start, width=600, height=100, bg='black')
        self.midle_frame = tk.Frame(self.start, width=600, height=350, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.footer_frame = tk.Frame(self.start, width=600, height=50, bg='black')
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
        self.midle_button_client = tk.Button(self.midle_frame, text='Client', fg='black', bg='lightgreen', font=('helvetica', 15), command=self.open_client)
        self.midle_button_client.pack(pady=10)
        self.midle_label_2 = tk.Label(self.midle_frame, text='or', bg='black', fg='white', font=('helvetica', 15))
        self.midle_label_2.pack(pady=10)
        self.midle_button_admin = tk.Button(self.midle_frame, text='Admin', fg='black', bg='orange', font=('helvetica', 15), command=self.open_admin)
        self.midle_button_admin.pack(pady=10)
        self.midle_label_3 = tk.Label(self.midle_frame, text='If running as admin, please enter password:', bg='black', fg='white', font=('helvetica', 15))
        self.midle_label_3.pack(pady=10)
        self.midle_entry = tk.Entry(self.midle_frame,show='*', bg='black', fg='lightgreen', font=('helvetica', 15), justify='center', insertbackground='lightgreen')
        self.midle_entry.pack(pady=10)
        self.midle_entry.bind('<Return>', lambda event:self.open_admin())

        # footer label
        self.footer_label_1 = tk.Label(self.footer_frame, text='by Rat Masters', bg='black', fg='white', font=('helvetica', 10))
        self.footer_label_1.pack()
        
        self.start.mainloop()

    #Button functions
    def open_client(self):
        self.start.destroy()        
        #self.client_window = ClientWindow()
        subprocess.call(['python', 'main_client.py'])

    def open_admin(self):        
        if self.midle_entry.get() != "rotta":
            showinfo(title="PASSWORD INCORRECT!", message="Please enter the correct password!")
            self.midle_entry.delete(0,END)
        else:
            self.start.destroy()           
            #self.admin_window = AdminWindow()
            subprocess.run(['python','main_server.py'])
            

if __name__ == "__main__":
    app = StartWindow()
    

        


 