import socket
import sys
import json
#from threading import Thread
import re
import random

class Inscription :
    def __init__(self):
        self.servAdd = ('localhost',3000)
        self.inscription = ({"request": "subscribe", "port": 8888, "name": "sosoj", "matricules": ["21255"]})
        self.port = 8888


    def transfo(self, file):
        data = json.dumps(file).encode()
        return data
    
    def inscri(self):
        sock = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
        try:
            sock.connect(self.servAdd)
            sock.send(bytes(self.transfo(self.inscription),'utf_8'))
            received = sock.recv(100000)
        finally:
            sock.close()
    
    def pong(self):       
        pong = self.transfo({"response": "pong"})
        return pong

    def ia(self):
        s = socket.socket()      
        s.bind(('localhost', self.port))        
        print ("socket binded to %s" %(self.port))
        s.listen(100000)    
        print ("socket is listening")           

    def resp_state(self):
        t = demande
        z = str(t)
        pattern = r'(?:"tile":)'
        p = re.compile(pattern)
        res = p.search(z)
        g = res.start()
        gs = g+8
        ge = gs + 60
        tuile = z[3111:3171]
        tile = json.loads(tuile)
        return tuile
        
    
    def move_played(self):
        gates = ['A','B','C','D','E','F','G','H','I','J','K','L']
        the_move_played = {"tile": self.resp_state(), "gate": gates[random.randint(0,len(gates)-1)] , "new_position": None}
        return the_move_played

    def resp_move(self):
        move = self.transfo({"response": "move", "move": self.move_played, "message": "Fun message"})
        return move

        

i = Inscription()
i.inscri()

s = socket.socket()      
s.bind(('localhost', i.port))        
print ("socket binded to %s" %(i.port))
s.listen(100000)    
print ("socket is listening") 
while True:
    c, addr = s.accept()    
    print ('Got connection from', addr )
    demande = c.recv(200000) #nbr de caractère recu
    if demande == b'{"request": "ping"}':
        c.send(bytes(i.pong(),'utf_8'))
        print('pong')
    else:
        print('else')
        c.send(bytes(i.resp_move(),'utf_8'))
           
        
c.close()
