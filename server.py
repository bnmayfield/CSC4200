import socket
import sys
import struct

# python3 server.py 8001 serverLogFile.txt
#tcpdump -i ens4 dst 34.28.255.197 -w project3.pcap -c 20

#packet section
h_message = 'Hello'
packet_hello = struct.pack('!III',17,1,len(h_message))
packet_hello += h_message.encode()

s_message = 'SUCCESS'
packet_success = struct.pack('!III',17,2,len(s_message))
packet_success += s_message.encode()



#Reading arguments
port = int(sys.argv[1])
logFileName = sys.argv[2]


#making socket
sock = socket.socket()
print ("Socket made")
sock.bind(('', port))
sock.listen(5)
print("Socket is listening")

#opening log file
logFile = open(logFileName, "a")



while True:
    client, address = sock.accept()
    print("Received connection from: ", address)
    logFile.write('Received Connection from: '+ str(address) +'\n')
    while True:
        clientPacket= client.recv(struct.calcsize('!III'))
        version, message_type, length = struct.unpack('!III',clientPacket)
        print("Packet Received:",version, message_type, length)
        #message= client.recv(length).decode()
        #print(message)
        logFile.write('Client Packet (Version #, Message Type, Length): '+ str(version)+','+ str(message_type)+','+str(length)+'\n')

        if version != 17:
            print("VERSION DENIED")
            logFile.write('VERSION MISMATCH '+'\n')
        else:
            print("VERSION ACCEPTED")
            logFile.write('VERSION ACCEPTED '+'\n')
            message= client.recv(length).decode()
            print("Message:",message)
            logFile.write('Message: '+message+'\n')


        if message_type == 1:
            print("SENDING HELLO")
            client.sendall(packet_hello)
            logFile.write('SENDING HELLO '+'\n')
        elif message_type ==2 :
            print("EXECUTING COMMAND", message)
            logFile.write('EXECUTED COMMAND '+'\n')
            client.sendall(packet_success)
            client.close()
            print("Client Closed")
            break
        


    

    