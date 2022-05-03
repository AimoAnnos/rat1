import tkinter
from tkinter import END
#from PIL import Image, ImageTk
import os
import subprocess
import pyautogui
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface

#Root window
root = tkinter.Tk()
root.title("Dirty RAT")
root.geometry("500x500+500+200")
root.iconbitmap("rat.ico")
root.resizable(0,0)
root.config(bg="#0d223d")
#global nics
nics = []

#Framet
button_frame = tkinter.LabelFrame(root, width=500, height=100)
button_frame.pack()
output_frame = tkinter.Frame(root, bg='black', width=500, height=500)
output_frame.pack(padx=10, pady=(0,10))
output_frame.pack_propagate(0)

def ota_screeni():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print('screen taken')

def ipconfig():
    with subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read().decode('ISO-8859-1'))

def getNics() :
    cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName,Caption,DefaultIPGateway /format:rawxml'
    xml_text = check_output(cmd, creationflags=8)
    xml_root = fromstring(xml_text)
    
    keyslookup = {
        'DNSHostName' : 'hostname',
        'IPAddress' : 'ip',
        'IPSubnet' : '_mask',
        'Caption' : 'hardware',
        'MACAddress' : 'mac',
        'DefaultIPGateway' : 'gateway',
    }

    for nic in xml_root.findall("./RESULTS/CIM/INSTANCE") :
        # parse and store nic info
        n = {
            'hostname':'',
            'ip':[],
            '_mask':[],
            'hardware':'',
            'mac':'',
            'gateway':[],
        }
        for prop in nic :
            name = keyslookup[prop.attrib['NAME']]
            if prop.tag == 'PROPERTY':
                if len(prop):
                    for v in prop:
                        n[name] = v.text
            elif prop.tag == 'PROPERTY.ARRAY':
                for v in prop.findall("./VALUE.ARRAY/VALUE") :
                    n[name].append(v.text)
        nics.append(n)

        # creates python ipaddress objects from ips and masks
        for i in range(len(n['ip'])) :
            arg = '%s/%s'%(n['ip'][i],n['_mask'][i])
            if ':' in n['ip'][i] : n['ip'][i] = IPv6Interface(arg)
            else : n['ip'][i] = IPv4Interface(arg)
        del n['_mask']

    #return nics

    #clear the frame
    for widget in output_frame.winfo_children():
        widget.destroy()
    #print ip info into frame
    text = tkinter.Label(output_frame, text=nics[0]['ip'][0],bg='black', fg='green')
    text.pack()
    # save ip into ip.txt
    with open ('ip.txt', 'w') as ip:
        text=str(nics[1]['ip'][0])
        text = text[0:-3]
        ip.write(text)

#Define colors and fonts
light_gray = '#f3f3f3'
mid_gray =  '#6c8794'
dark_gray = '#4c5f65'
light_green = '#78dfc7'
white_green = '#edefe0'
dark_green = '#78dfc7'
button_font = ('Calibri', 12)

#text_entry = tkinter.Entry(input_frame, width=40)
#text_entry.grid(row=0, column=0, padx=4, pady=4)
#output_frame.grid_propagate(0)
#frame1 = tkinter.Frame(root, bg='black', width=500, height=100)

#image = tkinter.PhotoImage(file="rat.png")

ip_button = tkinter.Button(button_frame, text='Get IP', font=button_font, bg=light_gray, command=getNics)
ip_button.grid(row=0,column=0,padx=5,pady=5, sticky='W')
server_button = tkinter.Button(button_frame, text="Server", font=button_font, bg=light_gray, command=lambda:os.system('main_server.py'))
server_button.grid(row=0,column=1,padx=5,pady=5, sticky="W")
client_button = tkinter.Button(button_frame, text=('Client'), font=button_font, bg=light_gray, command=lambda:os.system('main_client.py'))
client_button.grid(row=0, column=2,padx=5,pady=5)
screenshot_button = tkinter.Button(button_frame, text='Screen', font=button_font, bg=light_gray, command=ota_screeni)
screenshot_button.grid(row=0, column=3,padx=5,pady=5, sticky='W')
quit_button = tkinter.Button(button_frame, text='Quit', font=button_font, bg=light_gray, command=root.destroy)
quit_button.grid(row=0,column=6,padx=5, pady=5,sticky='W')

root.mainloop()
