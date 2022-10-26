import sys
import socket
#34.125.218.135
#8001
sock = socket.socket()
print ("Socket successfully created")
server = sys.argv[1]
port = int(sys.argv[2])
logFileName = sys.argv[3]
print('This is the server input:', server )
print('This is the port input:', port )
print('This is the log file name input:', logFileName)

logFile = open(logFileName, "a")

sock.connect((server, port))  

print("Please enter the message for the server. HINT: Please include the word 'Network'")
clientMessage= input() 
sock.send(clientMessage.encode())
logFile.write('Client: '+ clientMessage +'\n')

serverMessage= sock.recv(1024).decode()
print (serverMessage)
logFile.write('Server: '+ serverMessage +'\n')

logFile.close()
sock.close()
print("Socket Closed")
