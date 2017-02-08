import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()              
s.connect(('127.0.0.1' , 9600))
data = s.recv(1024)
print(data)
s.close() 