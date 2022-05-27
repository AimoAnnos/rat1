import tkinter as tk
from tkinter import Tk, Text
import os
import subprocess

root = tk.Tk()
root.geometry("640x480")
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

child_env = dict(os.environ)
child_env["SDL_WINDOWID"] = str(frame.winfo_id())
child_env["SDL_VIDEODRIVER"] = "windib"
p = subprocess.Popen(["cmd.exe"], env=child_env)
def execute(code):
    command = cmd.get('1.0', 'end').split('\n')[-2]
    if command == 'exit':
        exit()
    cmd.insert('end', f'\n{subprocess.getoutput(command)}')


main = Tk()

cmd = Text(main)
cmd.pack()

cmd.bind('<Return>', execute)

main.mainloop()

