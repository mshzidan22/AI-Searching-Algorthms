
class edges:
    def __init__(self, start ,end ,weight):
        self.start = start
        self.end =end
        self.weight =weight
        
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_weight(self):
        return self.weight
    def __toString__(self):
        return self.get_start()

    
az=edges("A","Z",75)
za=edges("Z","A",75)
aS=edges("A","S",140)
sa=edges("S","A",140)
at=edges("A","T",118)
ta=edges("T","A",118)
oz=edges("O","Z",71)
zo=edges("Z","O",71)
os=edges("O","S",151)
so=edges("S","O",151)
tl=edges("T","L",111)
lt=edges("L","T",111)
lm=edges("L","M",70)
ml=edges("M","L",70)
md=edges("M","D",75)
dm=edges("D","M",75)
dc=edges("D","C",120)
cd=edges("C","D",120)
sf=edges("S","F",99)
fs=edges("F","S",99)
fb=edges("F","B",211)
bf=edges("B","F",211)
sr=edges("S","R",80)
rs=edges("R","S",80)
rp=edges("R","P",97)
pr=edges("P","R",97)
cr=edges("C","R",146)
rc=edges("R","C",146)
cp=edges("C","P",138)
pc=edges("P","C",138)
pb=edges("P","B",101)
bp=edges("B","P",101)
gb=edges("G","B",90)
bg=edges("B","G",90)
bu=edges("B","U",85)
ub=edges("U","B",85)
uh=edges("U","H",98)
hu=edges("H","U",98)
he=edges("H","E",86)
eh=edges("E","H",86)
uv=edges("U","V",142)
vu=edges("V","U",142)
vi=edges("V","I",92)
iv=edges("I","V",92)
iN=edges("I","N",87)
ni=edges("N","I",87)


#iN
#aS
    


    
    
    

graph = {'A': [az, aS, at],
         'T': [ta,tl],
         'L': [lt, lm],
         'M': [ml,md],
         'D': [dm, dc],
         'C': [cp,cr,cd],
         'P': [pb,pc,pr],
         'S': [sf,sr,sa,so],
         'R': [rp,rc,rs],
         'Z': [za,zo],
         'O': [oz,os],
         'F': [fs,fb],
         'B': [bg,bp,bu,bf],
         'G': [gb],
         'U': [ub,uh,uv],
         'E': [eh],
         'H': [he,hu],
         'V': [vu,vi],
         'I': [iv,iN],
         'N': [ni],
         }
a=list(graph["A"])
print(a[0].start)

#longest path first
def DFS(graph,start,goal):
    frontier =[start]
    explored =[]
    while frontier:
        #remove the longest path from frontier
        path = frontier.pop(frontier.index(max(frontier, key=len)))
        s = path[-1]
        explored.append(s)
        if s==goal: return path

        for neighouber in graph[s]:
            if neighouber.get_start not in explored and neighouber.get_start not in frontier:
                new_path = list(path)
                new_path.append(neighouber.get_start)
                frontier.append(new_path)
    return "no path found"


print(DFS(graph,'A','B'))

               

                 
        
        