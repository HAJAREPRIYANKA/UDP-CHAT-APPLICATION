import os
os.system("clear")

# for displaying title
import pyfiglet as py

# to import required modules
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
results = py.figlet_format("UDP CHAT APPLICATION", font= "bubble")
print(results)

ip = "192.168.43.54"
port = 2222

s.bind((ip,port))

dest_ip = input("\n\t\tEnter Reciever IP: ")
dest_port = 1111

dest_ip2 = input("\n\t\tEnter Reciever IP2: ")
dest_port2 = 3333

def recieve():
    while True:
      x = s.recvfrom(1024)
      msg = "Message Form {} : {}".format(x[1][0],x[0].decode())
      print(msg)

def send():
    while True:
      x = input("")
      s.sendto("{}".format(x).encode(), (dest_ip, dest_port)) 
      s.sendto("{}".format(x).encode(), (dest_ip2, dest_port2))
      if (("bye" in x) or ("exit" in x)):
        os._exit(1)

# Applying Multi-Threading
recieve = threading.Thread( target=recieve )
send = threading.Thread( target=send )

recieve.start()
send.start()
