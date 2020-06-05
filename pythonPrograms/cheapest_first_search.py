graph = {'A': [['Z',75],['S',140],['T',118]],
         'T': [['A',118],['L',111]],
         'L': [['T',111],['M',70]],
         'M': [['L',70],['D',75]],
         'D': [['M',75],['C',120]],
         'C': [['P',138],['R',146],['D',120]],
         'P': [['B',101],['C',138],['R',97]],
         'S': [['F',99],['R',80],['A',140],['O',151]],
         'R': [['P',97],['C',146],['S',80]],
         'Z': [['A',75],['O',71]],
         'O': [['Z',71],['S',151]],
         'F': [['S',99],['B',211]],
         'B': [['G',90],['P',101],['U',85],['F',211]],
         'G': [['B',90]],
         'U': [['B',85],['H',98],['V',142]],
         'E': [['H',86]],
         'H': [['E',86],['U',98]],
         'V': [['U',142],['I',92]],
         'I': [['V',92],['N',87]],
         'N': [['I',87]],
         }

def DFS(graph,start,goal):
    frontier =[start]
    explored =[]
    cost=[]
    while frontier:
        #remove the shortest cost path from frontier
        path = frontier.pop(frontier.index(max(frontier, key=len)))
  
        s = path[-1]
        explored.append(s)
        if s==goal: return path
        for neighouber,cost in graph[s]:
            if neighouber not in explored and neighouber not in frontier:
                new_path = list(path)
                new_cost = list(cost)
                new_path.append(neighouber)
                frontier.append(new_path)
                
    return "no path found"



print(DFS(graph, "A", "B"))