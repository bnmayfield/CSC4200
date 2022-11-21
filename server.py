import socket
import sys
import random
# python3 server.py 8001 serverLogFile.txt
#tcpdump -i ens4 dst 35.225.41.220 -w project2.pcap -c 20
port = int(sys.argv[1])
logFileName = sys.argv[2]

sock = socket.socket()
print ("Socket made")

sock.bind(('', port))

sock.listen(5)
print("this sock be listening")

logFile = open(logFileName, "a")

while True:
    client, address = sock.accept()
    print("Got an address: ", address)

    clientMessage= str(client.recv(1024))
    print(clientMessage)
    logFile.write('Client: '+ clientMessage +'\n')

    serverMessage="Hello, here is a random quote for you: "
    lines = open('quotes.txt').read().splitlines()
    serverMessage = serverMessage + random.choice(lines)
    client.send(serverMessage.encode())
    logFile.write('Server: '+ serverMessage +'\n')

    client.close()
    print("Client Closed")

    