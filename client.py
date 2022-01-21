import socket
HOST = '172.16.221.1'  
PORT = 12121        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    file = open("mydata_client_copy.txt", "w")
    data = client.recv(1024).decode()
    file.write(data)
    file.close()
    client.close()
    print("Disconnected from server")