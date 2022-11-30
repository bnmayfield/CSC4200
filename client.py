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

logFile = open(logFileName, "a")

sock.connect((server, port))  
sock.sendall(packet_hello)

while True:
    serverPacket= sock.recv(struct.calcsize('!III'))
    version, message_type, length = struct.unpack('!III',serverPacket)
    print("Packet Received: ",version, message_type, length)
    #message= sock.recv(length).decode()
    #print(message)
    logFile.write('Server Packet (Version #, Message Type, Length): '+ str(version)+','+ str(message_type)+','+str(length)+'\n')

    if version != 17:
        print("VERSION DENIED")
        logFile.write('VERSION MISMATCH '+'\n')
    else:
        print("VERSION ACCEPTED")
        logFile.write('VERSION ACCEPTED '+'\n')
        message= sock.recv(length).decode()
        print("Message:",message)
        logFile.write('Message: '+message+'\n')


    if message_type == 1:
        print("SENDING COMMAND")
        logFile.write('SENT COMMAND '+'\n')
        sock.sendall(packet_command)
    elif message_type ==2 and message == "SUCCESS":
        print("COMMAND SUCESSFUL")
        logFile.write('COMMAND WAS SUCCESSFUL '+'\n')
        sock.close()
        print("Socket Closed")
        break

logFile.close()
