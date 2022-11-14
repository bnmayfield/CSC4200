import socket

sock = socket.socket()
print ("Socket made")

port=8001

sock.bind(('', port))

sock.listen(5)
print("this sock be listening")

while True:
    client, adress = sock.accep()
    client.send("thanks for connecting")
    client.close()
    break