from re import sub
import tkinter
#from PIL import Image, ImageTk
import os
import subprocess

#Root window
root = tkinter.Tk()
root.title("Dirty RAT")
root.geometry("500x500")
root.iconbitmap("rat.ico")
root.resizable(0,0)
root.config(bg="#0d223d")

# def suorita():
#     os.system('attacker_new.py')

def ota_screeni():
    pass

def ipconfig():
    with subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read())

#Define colors and fonts
light_gray = '#f3f3f3'
mid_gray =  '#6c8794'
dark_gray = '#4c5f65'
light_green = '#78dfc7'
white_green = '#edefe0'
dark_green = '#78dfc7'
button_font = ('Arial', 12)

#Framet
button_frame = tkinter.LabelFrame(root, width=500, height=100)
button_frame.grid(padx=5, pady=5)
input_frame = tkinter.Frame(root, bg='black', width=500, height=100)
input_frame.grid(padx=10, pady=10)

text_entry = tkinter.Entry(input_frame, width=40)
text_entry.grid(row=0, column=0, padx=4, pady=4)
input_frame.grid_propagate(0)
#frame1 = tkinter.Frame(root, bg='black', width=500, height=100)

image = tkinter.PhotoImage(file="rat2.png")

quit_button = tkinter.Button(button_frame, text='Quit', font=button_font, bg=light_gray, command=root.destroy)
quit_button.grid(row=0,column=0,padx=5, pady=5,sticky='W')
hack_button = tkinter.Button(button_frame, text="Start", font=button_font, bg=light_gray, command=lambda:os.system('attacker_new.py'))
hack_button.grid(row=0,column=1,padx=5,pady=5, sticky="W")
screenshot_button = tkinter.Button(button_frame, text='Screen', font=button_font, bg=light_gray, command=ipconfig)
screenshot_button.grid(row=0, column=2,padx=5,pady=5, sticky='W')

root.mainloop()
