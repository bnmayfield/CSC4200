import socket
import sys


port = int(sys.argv[1])
logFileName = sys.argv[2]

sock = socket.socket()
print ("Socket made")

sock.bind(('', port))

sock.listen(5)
print("this sock be listening")

logFile = open(logFileName, "a")

#Read in the quote text file(?)

while True:
    client, address = sock.accept()
    print("Got an address: ", address)

    clientMessage= sock.recv(1024).decode()
    logFile.write('Client: '+ clientMessage +'\n')

    serverMessage = "Thanks for connecting"
    client.send(serverMessage)
    logFile.write('Server: '+ serverMessage +'\n')
    
    client.close()
    break