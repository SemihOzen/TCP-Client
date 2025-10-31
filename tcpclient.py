import socket
from time import sleep


def client_program():
    host = '10.142.1.191'
    port = 5550

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = 'merhaba'
    while True:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
		
        print('Received from server: ' + data)
		
        if data == 'Derdin ne senin?':
            message = input("oğrenci no")
        elif data == 'Kaydedildi. Görüşürüz.':
            break
        else:
            message = 'merhaba'

        sleep(0.5)

    client_socket.close()


if __name__ == '__main__':
    client_program()
