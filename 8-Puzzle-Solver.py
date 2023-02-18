#   Faraz Majid
#   20L-1162
#   Assignment 1
#   8-Puzzle Problem
import time
import copy
import queue

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def printPuzzle(list):
    i = 0
    print("---------------------")
    while i <= 8:
        print("| {} {} {} |\n".format(list[i+0], list[i+1], list[i+2]))
        i += 3
    print("---------------------\n")
    
class puzzle:

    def __init__(self,str,gl):
            if str.isnumeric() and len(str) == 9:
                self.initial = list(str)
                self.goal = list(gl)
                self.visited = []
                self.visited.append(self.initial)
#                print ("Initial State : ", self.initial)
#                print ("Goal State : ", self.goal)
            elif str.isnumeric():
                print("input is not 9 characters")
            else:
                print("input is not numeric")

    def isGoal(self):
        if self.initial == self.goal:
            return True
        return False

    def print(self):
        #print("--------------8-Puzzle--------------")
        print("Initial State : ", self.initial)
        print ("Goal State : ", self.goal)
        print("\n")
        
    def display(self):
        print("--------------Result--------------")
        print("Initial State : ", self.initial)
        print ("Goal State : ", self.goal)
        print("\n")
        
    def updatePuzzle(self,arr):
        self.initial = arr 
    # This will return list of possible next states 
    # i.e next level of Graph
    def possibleMoves(self):
        index_of_empty = self.initial.index('0')
        temp = [] 
        
        def move_right(num):
            temp.append(copy.deepcopy(self.initial))
            swapPositions(temp[num],index_of_empty,index_of_empty+1)

        def move_left(num):
            temp.append(copy.deepcopy(self.initial))
            swapPositions(temp[num],index_of_empty,index_of_empty-1)

        def move_up(num):
            temp.append(copy.deepcopy(self.initial))
            swapPositions(temp[num],index_of_empty,index_of_empty-3)

        def move_down(num):
            temp.append(copy.deepcopy(self.initial))
            swapPositions(temp[num],index_of_empty,index_of_empty+3)

        if index_of_empty == 0:
            move_down(0)
            move_right(1)
        elif index_of_empty == 1:
            move_down(0)     
            move_right(1)
            move_left(2)
        elif index_of_empty == 2:
            move_down(0)
            move_left(1)
        elif index_of_empty == 3:
            move_up(0)
            move_down(1)
            move_right(2)
        elif index_of_empty == 4:
            move_up(0)
            move_down(1)
            move_right(2)
            move_left(3)
        elif index_of_empty == 5:
            move_up(0)
            move_down(1)
            move_left(2)
        elif index_of_empty == 6:
            move_up(0)
            move_right(1)
        elif index_of_empty == 7:
            move_up(0)
            move_right(1)
            move_left(2)
        elif index_of_empty == 8:
            move_up(0)
            move_left(1)

        res = []
        for x in range(len(temp)):
            if temp[x] not in self.visited:
                res.append(temp[x])
                self.visited.append(temp[x])
            # else:
            #     print("Test",temp[x])
        # print(temp)
        # print("---------------------------------------")
        # print(res)
        # print("#######################################")

        return res

def DFS(puz):
    path_tree = dict() # Child is key Parent is Value
    s = queue.LifoQueue()
    s.put(puz.initial)
    start = time.time()
    time.sleep(0.01)
    _initial = puz.initial
    #print(start)
    print("--------DFS--------")
    node_count = 0
    explored = []
    while True:
        puz.updatePuzzle(s.get())
        node_count += 1
        if puz.isGoal():
            break
        explored = puz.possibleMoves()
        if explored == []:
            continue
        for i in range(len(explored)):
            s.put(explored[i])
            path_tree[str(explored[i])] = puz.initial
        t = time.time() - start
        tt = float(f'{t:.6f}')
        print("Time Taken : {} \tNode Count: {}".format(tt,node_count),end="\r")

    t = float(f'{time.time() - start:.5f}')
    node_count += len(explored)
    print("Time Taken : {} \tNode Count: {}".format(tt,node_count),end="\n")
    # puz.display()

    result = queue.LifoQueue()
    cost = 0
    x = puz.goal
    while not x == _initial:
        result.put(x)
        x = path_tree.get(str(x))
        cost += 1
        
    print("Path Cost: {}".format(cost))
        
    while not result.empty():
        printPuzzle(result.get())

def BFS(puz):
    path_tree = dict() # Child is key Parent is Value
    q = queue.Queue()
    q.put(puz.initial)
    _initial = puz.initial
    start = time.time()
    time.sleep(0.01)
    #print(start)
    print("--------BFS--------")
    node_count = 0
    explored = []
    while True:
        puz.updatePuzzle(q.get())
        node_count += 1
        if puz.isGoal():
            break
        explored = puz.possibleMoves()
        if explored == []:
            continue
        for i in range(len(explored)):
            q.put(explored[i])
            path_tree[str(explored[i])] = puz.initial
        t = time.time() - start
        tt = float(f'{t:.6f}')
        print("Time Taken : {} \tNode Count: {}".format(tt,node_count),end="\r")
        # print("Time Taken : {} \tNode Count: {} \tVisited: {}".format(tt,node_count,len(puz.visited)),end="\r")

    t = float(f'{time.time() - start:.5f}')
    node_count += len(explored)
    print("Time Taken : {} \tNode Count: {}".format(tt,node_count),end="\n")
    
    cost = 0
    result = queue.LifoQueue()
    cost = 0
    x = puz.goal
    while not x == _initial:
        result.put(x)
        x = path_tree.get(str(x))
        cost += 1
        
    print("Path Cost: {}".format(cost))
        
    while not result.empty():
        printPuzzle(result.get())

def IDS(puz):
    path_tree = dict() # Child is key Parent is Value
    _initial = puz.initial
    def DLS(puz,depth):
        path_tree.clear()
        q = queue.LifoQueue()
        q.put(puz.initial)
        start = time.time()
        time.sleep(0.01)
        #print(start)
        #print("--------DLS {} --------".format(depth))
        node_count = 0
        explored = []
        limit = 0
        while True:
            if(limit == depth):
                return False
            puz.updatePuzzle(q.get())
            node_count += 1
            if puz.isGoal():
                t = time.time() - start
                tt = float(f'{t:.6f}')
                print("Time Taken : {} \tNode Count: {}".format(tt,node_count))
                return True
            
            explored = puz.possibleMoves()
            if explored == []:
                continue
            for i in range(len(explored)):
                q.put(explored[i])
                path_tree[str(explored[i])] = puz.initial
                
            limit += 1
            t = time.time() - start
            tt = float(f'{t:.4f}')
            # print("Time Taken : {} \tNode Count: {}".format(tt,node_count),end="\r")
            # print("Time Taken : {} \tNode Count: {} \tVisited: {}".format(tt,node_count,len(puz.visited)),end="\r")
            

        # print("Node Count : ", node_count) 
        # print("Time Taken : ",  time.time() - start)
        t = float(f'{time.time() - start:.5f}')
        node_count += len(explored)
        print("--------DLS {} --------".format(depth),end="\r")
        #print("Time Taken : {} \tNode Count: {}".format(tt,node_count),end="\n")
        #puz.display()

    print("--------IDS--------")
    count = 1
    puzT = copy.deepcopy(puz)
    while not DLS(puzT,count):
        print("Searching     \t DLS {}".format(count),end="\r")
        time.sleep(0.01)
        print("Searching.    ",end="\r")
        time.sleep(0.01)
        print("Searching..   ",end="\r")
        time.sleep(0.01)
        print("Searching...  ",end="\r")
        time.sleep(0.01)
        print("Searching.... ",end="\r")
        time.sleep(0.01)
        print("Searching.....",end="\r")
        puzT = copy.deepcopy(puz)
        count += 1
    
    result = queue.LifoQueue()
    cost = 0
    x = puz.goal
    while not x == _initial:
        result.put(x)
        x = path_tree.get(str(x))
        cost += 1
        
    print("Path Cost: {}".format(cost))
        
    while not result.empty():
        printPuzzle(result.get())
        
    #puz.display()


     

print("\n")
print("--------------8-Puzzle--------------")
print("------------Faraz Majid-------------")
print("--------------20L-1162--------------\n")
initial = "120345678"
goal = "012345678"
initial = input("Enter Initial State (9 Digit Number): ")
goal = input("Enter Goal State (9 Digit Number): ")

puzA = puzzle(initial,goal)
puzA.print()
BFS(puzA)
print("------------------------------------\n")

puzB = puzzle(initial,goal)
#puzB.print()
DFS(puzB)
print("------------------------------------\n")

puzC = puzzle(initial,goal)
#puzC.print()
IDS(puzC)
print("------------------------------------\n")