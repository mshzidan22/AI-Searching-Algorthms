'''
Created on Nov 14, 2019

@author: MshzidanPC
'''

class Node:
    

    def __init__(self,name,neighbours=[],cost=[]):
        self.name= name
        self.setNeighbours(neighbours)
        self.setCost(cost)
        
        
    def setName(self,name):
        self.name = name
           
    def getName(self):
        return self.name
    
    def setNeighbours(self,neighbours =[]):
        self.neighbours= neighbours
        
    def getNeighbours(self):
        return self.neighbours
    
    def setCost(self,c=[]):
        self.costs ={}
        for c,n in zip(c,self.neighbours):
            self.costs.setdefault(n,c)
    
    def getCost(self,city):
        return self.costs.get(city)
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
    
A=Node("A",['Z', 'S', 'T'],[75,140,118])
T=Node("T",['A', 'L'],[118,111])
L=Node("L",['T', 'M'],[111,70])
M=Node("M",['L', 'D'],[70,75])
D=Node("D",['M', 'C'],[75,120])
C=Node("C",['P', 'R', 'D'],[138,146,120])
P=Node("P",['B', 'C', 'R'],[101,138,97])
S=Node("S",['F', 'R', 'A','O'],[99,80,140,151])
R=Node("R",['P', 'C', 'S'],[97,146,80])
Z=Node("Z",['A', 'O'],[75,71])
O=Node("O",['Z', 'S'],[71,151])
F=Node("F",['S', 'B'],[99,211])
B=Node("B",['G', 'P', 'U','F'],[90,101,85,211])
G=Node("G",['B'],[90])
U=Node("U",['B', 'H', 'V'],[85,98,142])
E=Node("E",['H'],[86])
H=Node("H",['E', 'U'],[86,98])
V=Node("V",['U', 'I'],[142,92])
I=Node("I",['V', 'N'],[92,87])
N=Node("N",['I'],[87])


graph = { A: [Z,S,T],
          T: [A,L],
          L: [T,M],
          M: [L,D],
          D: [M,C],
          C: [P,R,D],
          P: [B,C,R],
          S: [F,R,A,O],
          R: [P,C,S],
          Z: [A,O],
          O: [Z,S],
          F: [S,B],
          B: [G,P,U,F],
          G: [B],
          U: [B,H,V],
          E: [H],
          H: [E,U],
          V: [U,I],
          I: [V,N],
          N: [I],
         }

def indexAndCosts(frontier,start):
    
    #this function returns the index of the shortest cost and it's cost from frontier
    total=0
    l=[]
    
    for a in frontier:
       
        for b in a:
            if b == a[0]:
                c=b
                
            else:
                total =b.getCost(c.getName()) + total
                c=b
        l.append(total)
        total=0
    
    return l.index(min(l)),min(l)
    
    
    
    

def UCS(graph,start,goal):
    frontier =[[start]]
    explored =[]
    while frontier:
        #remove the shortest path from frontier
        index,cost=indexAndCosts(frontier, start)
        path = frontier.pop(index)
        
        print("this is fronter  ",frontier)
        print("this is path    ",path)
        s = path[-1]
        explored.append(s)
        if s==goal: return path,cost
        for neighouber in graph[s]:
            if neighouber not in explored and neighouber not in frontier:
                new_path = list(path)
                new_path.append(neighouber)
                frontier.append(new_path)
                print("this is the second fronter",frontier)
    return "no path found"

print(UCS(graph,A,B))

