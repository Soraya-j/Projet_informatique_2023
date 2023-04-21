import socket
import sys
import json
import re
import random

class Inscription :
    def __init__(self):
        self.servAdd = ('localhost',3000)
        self.inscription = ({"request": "subscribe", "port": 8888, "name": "sosoj", "matricules": ["21255"]})
        self.port = 8888


    def transfo(self, file):
        data = json.dumps(file).encode('utf_8')
        return data
    
    def inscri(self):
        sock = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
        try:
            sock.connect(self.servAdd)
            sock.send(self.transfo(self.inscription))
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

class Game:

    def resp_state(self):
        print('resp_state')
        z = str(t)                
        tuile = re.search('tile": (.+?), "target', z).group(1)
        print(tuile)
        tile = json.loads(tuile)
        return tile
        
    
    def move_played(self):
        print('move_played')
        gates = ['A','B','C','D','E','F','G','H','I','J','K','L']
        letter = gates[random.randint(0,len(gates)-1)]
        the_move_played = {"tile": self.resp_state(), "gate": letter , "new_position": 0}   
        return the_move_played

    def resp_move(self):
        print('resp_move')
        move = i.transfo({"response": "move", "move": self.move_played(), "message": "I played"})
        return move

        
                                                         
i = Inscription()
g = Game()
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
        c.send(i.pong())
        print('pong')
    else:
        t = demande
        print('else')
        c.send(g.resp_move())
           
        
c.close()
