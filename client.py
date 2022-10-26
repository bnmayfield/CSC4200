# Import sys module
import sys
import socket

sock = socket.socket()
print ("Socket successfully created")

server = str(sys.argv[1])
port = sys.argv[2]
print('This is the server input:', server )
print('This is the port input:', port )
#logFile = sys.argv[3]

client=server
 
sock.connect((server, port))  
#print ("socket binded to %s" %(port)) 
client=server
     
 #message from user
client.send('Thank you for the Network message'.encode())
print (sock.recv(1024).decode())
client.close()
