import socket

UDP_IP = "10.160.108.101"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


MESSAGE=input("")
sock.connect((UDP_IP, UDP_PORT))
sock.send(MESSAGE.encode())

data, addr= sock.recvfrom(1024)
print("Message Serveur1 : ", data)


sock.send(MESSAGE.encode())
code = " "
code = (data[0]<<24 or data[1]<<16 or data[2]<<8 or data[3])
code, addr= sock.recvfrom(1024)
print("Code= ", code)










 
