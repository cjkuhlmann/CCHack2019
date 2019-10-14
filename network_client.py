import socket

class Network():
    def __init__(self):
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.connect(('localhost',7777))
        print("conected")
        
    def send_data(self,msg):
        sent = self.soc.sendall(msg)
        data = self.soc.recv(1024)
        print(data)

N = Network()
N.send_data(b"Sample data")
