
import tkinter as tk
from tkinter import ttk, BOTH
from tkinter.messagebox import showinfo

class AdminWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # configure the root window
        self.title('Admin Window')
        self.iconbitmap('icons/rat.ico')
        self.geometry('1200x900+200+50')
        self.config(bg='black')
        #self.resizable(0,0)

        # setting layout frames
        self.header_frame = tk.Frame(self, width=1200, height=100, bg='black')
        self.midle_frame = tk.Frame(self,width=1200, height=800, bg='black')
        self.midle_left_frame = tk.Frame(self.midle_frame, width=750, height=700, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.midle_right_frame = tk.Frame(self.midle_frame, width=350, height=700, bg='black', highlightbackground='lightgreen', highlightcolor='lightgreen', highlightthickness=2, bd=0)
        self.footer_frame = tk.Frame(self, width=1200, height=50, bg='black')
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
        self.midle_left_label_1 = tk.Label(self.midle_left_frame, text='CMD', bg='black', fg='white', font=('helvetica', 15))
        self.midle_left_label_1.pack(pady=10)
        self.midle_left_text = tk.Text(self.midle_left_frame, width=100, height=35, bg='black', fg='lightgreen', font=('helvetica',  10), insertbackground='lightgreen')
        self.midle_left_text.pack(padx=10, pady=10)
        self.midle_left_bottom_frame = tk.Frame(self.midle_left_frame, bg='black', width=700, height=145)
        self.midle_left_bottom_frame.pack()
        self.midle_left_bottom_data_button = tk.Button(self.midle_left_bottom_frame, width=15, text='Database', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_left_bottom_data_button.grid(row=0, column=1, padx=10, pady=(10, 20))
        self.midle_left_bottom_info_button = tk.Button(self.midle_left_bottom_frame, width=15, text='Info / settings', bg='lightgreen', fg='black', font=('helvetica', 15))
        self.midle_left_bottom_info_button.grid(row=0, column=2, padx=10, pady=(10, 20))
        self.midle_left_bottom_exit_button = tk.Button(self.midle_left_bottom_frame, width=15, text='Exit', bg='orange', fg='black', font=('helvetica', 15))
        self.midle_left_bottom_exit_button.grid(row=0, column=3, padx=10, pady=(10, 24))

        self.midle_right_label_1 = tk.Label(self.midle_right_frame, text='Chat', bg='black', fg='white', font=('helvetica', 15))
        self.midle_right_label_1.pack(pady=10)
        self.midle_right_text = tk.Text(self.midle_right_frame, width=40, height=21, bg='black', fg='lightgreen', font=('helvetica',  10), insertbackground='lightgreen')
        self.midle_right_text.pack(padx=10, pady=10)
        self.midle_right_label_2 = tk.Label(self.midle_right_frame, text='Client quick buttons', bg='black', fg='white', font=('helvetica', 15))
        self.midle_right_label_2.pack(pady=10)
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
        

if __name__ == "__main__":
    app = AdminWindow() 
    app.mainloop()

 