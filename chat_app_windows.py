import os
os.system("cls")
 
# for displaying title
import pyfiglet as py


# importing required modules...
import socket
import threading

# AF_INET = Network Address Family : ipv4
# SOCK_DGRAM = DataGram Socket : UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("cls")
results = py.figlet_format("UDP CHAT APPLICATION", font= "bubble")
print(results)


# System IP
ip = "192.168.43.187"
port = 1111

# Reciever IP
sendip = input("\n\t\tEnter Reciever IP : ")
sendport = 2222

sendip_2 = input("\n\t\tEnter Reciever IP2 : ")      
sendport_2 = 3333

# Binding system IP and port
s.bind((ip, port))

# Function for sending message
def send():
	while True:
		x = input("")
		s.sendto("{}".format(x).encode(), (sendip, sendport))
		s.sendto("{}".format(x).encode(), (sendip_2, sendport_2))
		if (("bye" in x) or ("exit" in x)):
			os._exit(1)

# Function for recieving message
def recieve():
	while True:
		x = s.recvfrom(1024)
		msg = "Message Form {} : {}".format(x[1][0],x[0].decode())
		print(msg)


# Applying Multi-Threading
send = threading.Thread( target=send )
recieve = threading.Thread( target=recieve )

send.start()
recieve.start()