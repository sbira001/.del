import socket
HOST = '172.16.221.1'  
PORT = 12121    
file = open("mydata.txt","r")
data = file.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    while True:
        conn, addr = server.accept()
        print('Connected by', addr)
        conn.send(data.encode())
        file.close()
        print('Closing connection from server')
        conn.close()