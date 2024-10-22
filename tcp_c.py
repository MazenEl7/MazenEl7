import socket

host = "192.168.1.14"
port = 9998

def loop():
    
    text = input("Write: ")
    
    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    client.connect((host,port))

    client.send(b""+ text.encode())

    response = client.recv(4096)
    print(response.decode())
    again = input("Do you want to sent again [y],[n]: ")
    if again == 'y':
        loop()
    else:
        client.close()
 
loop()

