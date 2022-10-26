# Import sys module
import sys
import socket

s = socket.socket()
print ("Socket successfully created")

server = sys.argv[1]
port = sys.argv[2]
#logFile = sys.argv[3]
client=server
s.bind((server, port))   
print ("socket binded to %s" %(port)) 
client=server
s.listen(5)     

while True:
  message = s.accept() 
  print ('Got message:', message )
  client.send('Thank you for the message'.encode())
  client.close()
  break
