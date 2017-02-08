import socket 
x=1
st = "hello world"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host=socket.gethostname()
s.bind(('localhost' , 9600))
s.listen(5)
while x==1:
	c,a = s.accept()
	print("received connection from " , a)
	c.send(st.encode('utf-8'))
	c.close()
