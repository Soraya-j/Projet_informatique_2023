import socket
import sys
import json

servAdd = ('localhost',3000)
inscription = {
    "request": "subscribe",
    "port": 8888,
    "name": "sosoj",
    "matricules": ["21255"]
 }
 
data = json.dumps(inscription)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(servAdd)
    sock.send(bytes(data,'utf_8'))
    received = sock.recv(3000)
finally:
    sock.close()

print ("Sent:     {}".format(data))
print ("Received: {}".format(received))



s = socket.socket()        
pong = {
   "response": "pong"
}
resp = json.dumps(pong)
print ("Socket successfully created")
ping = {
   "request": "ping"
}
recv = json.dumps(ping)

port = 8888            
s.bind(('localhost', port))        
print ("socket binded to %s" %(port))

s.listen(3000)    
print ("socket is listening")           
 
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  c.send(bytes(resp,'utf_8'))
  print(pong)
  demande = c.recv(3000)
    
c.close()
