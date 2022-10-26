import sys
import socket
#34.125.218.135
#8001
sock = socket.socket()
print ("Socket successfully created")

server = sys.argv[1]
port = int(sys.argv[2])
#logFile = sys.argv[3]
print('This is the server input:', server )
print('This is the port input:', port )

sock.connect((server, port))  

print("Please enter the message for the server. HINT: Please include the word 'Network'")
clientMessage= input() 
#print(clientMessage)  
#message from user
sock.send(clientMessage.encode())
serverMessage= sock.recv(1024).decode()
print (serverMessage)
sock.close()
print("Socket Closed")
