import socket
import sys


port = int(sys.argv[1])
logFileName = sys.argv[2]

sock = socket.socket()
print ("Socket made")

sock.bind(('', port))

sock.listen(5)
print("this sock be listening")

#Read in the quote text file(?)

while True:
    client, address = sock.accept()
    print("Got an address: ", address)
    clientMessage= sock.recv(1024).decode()
    client.send("thanks for connecting")
    client.close()
    break