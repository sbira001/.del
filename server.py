import socket
HOST = socket.gethostbyname('ipc_server_dns_name') 
PORT = 12121    
file = open("/server/server_persistent_storage/mydata.txt","r")
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