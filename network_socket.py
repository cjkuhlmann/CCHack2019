import socket

host = ""
port = 7777

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_ip = socket.gethostbyname(socket.gethostname())
print(my_ip)
c.bind(('',25565))
c.listen(1)
while True:
    client,addr = c.accept()
    print(addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        print(data)
