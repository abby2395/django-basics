import socket

# create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect with the url and host
mysock.connect(('google.com', 80))

cmd = 'GET http://google.com HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = '')

mysock.close()