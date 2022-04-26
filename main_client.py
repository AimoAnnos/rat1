import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class MainClient(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x100+500+500')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me', command=self.button_clicked)
        #self.button['command'] = self.button_clicked
        self.button.pack(padx=20, pady=20)


    def button_clicked(self):
        showinfo(title='Information',
        message='Hello, Tkinter!')

    

    


if __name__ == "__main__":
    app = MainClient()
    app.mainloop()

