from tkinter import Tk, Text
import subprocess


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