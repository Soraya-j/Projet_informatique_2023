import socket
import json
import random

# def turn_tile(tile):
#     res = copy.deepcopy(tile)
#     res["N"] = tile["E"]
#     res["E"] = tile["S"]
#     res["S"] = tile["W"]
#     res["W"] = tile["N"]
#     return res
coord = {
    (0,0):0, (0,1):1, (0,2):2, (0,3):3, (0,4):4, (0,5):5, (0,6):6, 
    (1,0):7, (1,1):8, (1,2):9, (1,3):10, (1,4):11, (1,5):12, (1,6):13,
    (2,0):14, (2,1):15, (2,2):16, (2,3):17, (2,4):18, (2,5):19, (2,6):20,
    (3,0):21, (3,1):22, (3,2):23, (3,3):24, (3,4):25, (3,5):26, (3,6):27,
    (4,0):28, (4,1):29, (4,2):30, (4,3):31, (4,4):32, (4,5):33, (4,6):34,
    (5,0):35, (5,1):36, (5,2):37, (5,3):38, (5,4):39, (5,5):40, (5,6):41,
    (6,0):42, (6,1):43, (6,2):44, (6,3):45, (6,4):46, (6,5):47, (6,6):48,   
}
list_of_coord = list(coord.keys())
#print(len(list_of_coord))
direction = {
    "N": {"coords": (0, -1), "inc": -7, "opposite": "S"},
    "S": {"coords": (0, 1), "inc": 7, "opposite": "N"},
    "W": {"coords": (-1, 0), "inc": -1, "opposite": "E"},
    "E": {"coords": (1, 0), "inc": 1, "opposite": "W"},
    (0,-1): {"name": "N"},
    (0,1): {"name": "S"},
    (-1,0): {"name": "W"},
    (1,0): {"name": "E"},
}
dico_num_tuile = {
    'N': [0,1,2,3,4,5],
    'E': [6,13,20,27,34,41],
    'S': [43,44,45,46,47,48],
    'W': [7,14,21,28,35,42],
    'R': [8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31,32,33,36,37,38,39,40]
}
Gates = {
    "V1" : [1, 8, 15, 22 , 29, 36, 43],
    "V2" : [3, 10, 17, 24, 31, 38, 45],
    "V3" : [5, 12, 19, 26, 33, 40, 47],
    "H1" : [7, 8, 9, 10, 11, 12, 13],
    "H2" : [21, 22, 23, 24, 25, 26, 27],
    "H3" : [35, 36, 37, 38, 39, 40, 41]
        }
class Queue:
	def __init__(self):
		self.data = []

	def enqueue(self, value):
		self.data.append(value)

	def dequeue(self):
		return self.data.pop(0)

	def isEmpty(self):
		return len(self.data) == 0

class Inscription :
    def __init__(self):
        self.servAdd = ('localhost',3000)
        self.inscription = {"request": "subscribe", "port": 8888, "name": "sosoj", "matricules": ["21255"]}
        self.port = 8888
    def transfo(self, file):
        data = json.dumps(file).encode('utf_8')
        return data
    def inscri(self):
        sock = socket.socket()
        try:
            sock.connect(self.servAdd)
            sock.send(self.transfo(self.inscription))
            received = sock.recv(100000)
        finally:
            sock.close()
    def pong(self):       
        pong = self.transfo({"response": "pong"})
        return pong

class Game:
    def resp_move(self):
        move = i.transfo({"response": "move", "move": self.move_played(), "message": "I played"})
        print('à répondu au move')
        return move
    def prob_gates(self):
        gates = []
        for elem in Gates :
            if self.actual_pos() not in Gates[elem]: 
                if self.new_pos() not in Gates[elem]:
                    if elem == 'V1':
                        gates.append('A')
                        gates.append('I')
                    if elem == 'V2':
                        gates.append('B')
                        gates.append('H')
                    if elem == 'V3':
                        gates.append('C')
                        gates.append('G')
                    if elem == 'H1':
                        gates.append('L')
                        gates.append('D')
                    if elem == 'H2':
                        gates.append('K')
                        gates.append('E')
                    if elem == 'H3':
                        gates.append('F')
                        gates.append('J')
        return gates
    def move_played(self):
        gates = self.prob_gates()
        letter = gates[random.randint(0,len(gates)-1)]
        print('letter : ',letter)
        the_move_played = {"tile": self.free_tile(), "gate": letter , "new_position": self.new_pos()}   
        return the_move_played
    def free_tile(self):              
        tile = receipt['state']['tile']
        print('free_tile:') 
        print(tile)
        return tile
    def new_pos(self):
        print('fonction bfs:::')
        self.BFS(list_of_coord[self.actual_pos()], self.my_target())    
        print('test tile : ', self.new_tile(self.actual_pos()))
        path = self.path(self.new_tile(self.actual_pos()))
        if path == []:
            add = 0
        else :
            add = path[random.randint(0,len(path)-1)]
            print('add :')
            print(add)
        new_position = int(self.actual_pos()) + add
        print('position actuelle :')
        print(self.actual_pos())
        print('nouvelle position :') 
        print(new_position)
        return new_position 
    def actual_pos(self):
        current = receipt['state']['current']
        current_pos = receipt['state']['positions']
        actual = current_pos[int(current)]
        return actual
    def path(self, tile):
        #tile = self.new_tile(self.actual_pos())
        # print('test tile :')
        # print(tile)
        cardinal = ['N', 'E', 'S', 'W']
        path = []
        for elem in cardinal:
            if tile[elem] == True:
                path.append(direction[elem]['inc'])                
        print('path:')
        print(path)
        return path
    def new_tile(self, act_pos):
        new_tile = {}
        board = receipt['state']['board']
        if act_pos in dico_num_tuile['N'] :
            new_tile['N'] = False
            if act_pos == 0 :
                new_tile['W'] = False
                cardinal = ['E','S']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            else :
                cardinal = ['E','S','W']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            return new_tile
        elif act_pos in dico_num_tuile['E'] :
            new_tile['E'] = False
            if act_pos == 6 :
                new_tile['N'] = False
                cardinal = ['W','S']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            else :
                cardinal = ['N','S','W']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            return new_tile
        elif act_pos in dico_num_tuile['S'] :
            new_tile['S'] = False
            if act_pos == 48 :
                new_tile['E'] = False
                cardinal = ['N','W']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            else :
                cardinal = ['N','E','W']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            return new_tile
        elif act_pos in dico_num_tuile['W'] :
            new_tile['W'] = False
            if act_pos == 42 :
                new_tile['S'] = False
                cardinal = ['N','E']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            else :
                cardinal = ['N','E','S']
                for elem in cardinal :
                    new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            return new_tile
        elif act_pos in dico_num_tuile['R'] :
            cardinal = ['N','E','S', 'W']
            for elem in cardinal :
                new_tile[elem] = all([board[act_pos][elem],board[act_pos + direction[elem]['inc']][direction[elem]['opposite']]])
            return new_tile
    def my_target(self):
        target = receipt['state']['target']
        res = []
        print('my target :')
        print(target)
        i = 0
        board = receipt['state']['board']
        while i < len(board) - 1 :
            i += 1
            if receipt['state']['board'][i]['item'] == target :
                pos_tuile_target = i
                print('my pos : ', self.actual_pos())
                print('pos_tuile_target : ', pos_tuile_target)
                res.append(pos_tuile_target)
                break 
        return res
    
    def BFS(self,start, pos_target):
        q = Queue()
        q.enqueue(start)
        while not q.isEmpty():
            node = q.dequeue()
            if node in pos_target:
                print("J'AI TROUVÉ UN TRÉSOR")
            for elem in self.successors(node):
                    q.enqueue(elem)
            node = None

        res = []
        while node is not None:
            res.append(node)
            print('liste du chemin : ',list(reversed(res)))
        print('liste du chemin : ',list(reversed(res)))

    def successors(self, node):
        directions = [direction['N']['coords'], direction['E']['coords'], direction['S']['coords'], direction['W']['coords']]
        res = []
        board = receipt['state']['board']
        x, y = node
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            try :
                match_tuile = coord[(nx,ny)]
                dir = direction[(dx,dy)]['name']
                if board[match_tuile][dir] and board[match_tuile + direction[dir]['inc']][direction[dir]['opposite']]:                   
                        res.append((nx, ny))
            except KeyError:
                print('error_out of the board : ',(nx,ny))
                dx = None
                dy = None
        print('res : ',res)
        return res
    



i = Inscription()
g = Game()

i.inscri()
s = socket.socket()      
s.bind(('localhost', i.port))        
s.listen(100000)    
 
while True:
    c, addr = s.accept()    
    receipt = json.loads(c.recv(200000)) #conver en dico (20... = nbr de caractère rec autorisé)
    if receipt['request'] == "ping":
        c.send(i.pong())
        print('pong')
    if receipt['request'] == 'play':
        print(receipt['request'])
        c.send(g.resp_move())
        g.my_target()
        print('errors :')
        print(receipt['errors'])
           
        
c.close()
