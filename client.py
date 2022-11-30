import sys
import socket
import struct
#34.173.101.159
#8001

#INSTANCE 2 SERVER
# python3 client.py 34.173.101.159 8001 logFile.txt

#packet section
h_message = 'Hello'
packet_hello = struct.pack('!III',17,1,len(h_message))
packet_hello += h_message.encode()
#print('Hello Packet: ',packet_hello)
c_message = 'LIGHTON'
packet_command = struct.pack('!III',17,2,len(c_message))
packet_command += c_message.encode()
#print('Command Packet: ',packet_command)



sock = socket.socket()
print ("Socket successfully created")
server = sys.argv[1]
port = int(sys.argv[2])
logFileName = sys.argv[3]
print('This is the server input:', server )
print('This is the port input:', port )
print('This is the log file name input:', logFileName)

#logFile = open(logFileName, "a")

sock.connect((server, port))  
sock.sendall(packet_hello)
#print("Please enter the message for the server. HINT: Please include the word 'Network'")
#clientMessage= input() 
#sock.send(clientMessage.encode())
#logFile.write('Client: '+ clientMessage +'\n')

#serverMessage= sock.recv(1024).decode()
#print (serverMessage)
#logFile.write('Server: '+ serverMessage +'\n')

#logFile.close()
sock.close()
print("Socket Closed")
