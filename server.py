import socket
import sys
#import random
import struct

# python3 server.py 8001 serverLogFile.txt
#tcpdump -i ens4 dst 35.225.41.220 -w project2.pcap -c 20

#packet section
h_message = 'Hello'
packet_hello = struct.pack('!III',17,1,len(h_message))
packet_hello += h_message.encode()

c_message = 'LIGHTON'
packet_command = struct.pack('!III',17,2,len(c_message))
packet_command += c_message.encode()



#Reading arguments
port = int(sys.argv[1])
logFileName = sys.argv[2]


#making socket
sock = socket.socket()
print ("Socket made")
sock.bind(('', port))
sock.listen(5)
print("this sock be listening")

#opening log file
logFile = open(logFileName, "a")



while True:
    client, address = sock.accept()
    print("Received connection from: ", address)
    logFile.write('Received Connection from: '+ str(address) +'\n')

    clientPacket= client.recv(struct.calcsize('!III'))
    version, message_type, length = struct.unpack('!III',clientPacket)
    print(version, message_type, length)
    message= client.recv(length).decode()
    print(message)
    logFile.write('Client Packet (Version #, Message Type, Length, Message): '+ str(version)+','+ str(message_type)+','+str(length)+','+message+'\n')

   # serverMessage="Hello, here is a random quote for you: "
    #lines = open('quotes.txt').read().splitlines()
    #serverMessage = serverMessage + random.choice(lines)
    #client.send(serverMessage.encode())
   # logFile.write('Server: '+ serverMessage +'\n')

    client.close()
    print("Client Closed")

    