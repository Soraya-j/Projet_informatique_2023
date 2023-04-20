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