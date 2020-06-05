graph = {'A': ['Z', 'S', 'T'],
         'T': ['A','L'],
         'L': ['T', 'M'],
         'M': ['L','D'],
         'D': ['M', 'C'],
         'C': ['P','R','D'],
         'P': ['B','C','R'],
         'S': ['F','R','A','O'],
         'R': ['P','C','S'],
         'Z': ['A','O'],
         'O': ['Z','S'],
         'F': ['S','B'],
         'B': ['G','P','U','F'],
         'G': ['B'],
         'U': ['B','H','V'],
         'E': ['H'],
         'H': ['E','U'],
         'V': ['U','I'],
         'I': ['V','N'],
         'N': ['I'],
         }

#longest path first
def DFS(graph,start,goal):
    frontier =[start]
    explored =[]
    while frontier:
        #remove the longest path from frontier
        path = frontier.pop(frontier.index(max(frontier, key=len)))
        print("this is fronter  ",frontier)
        print("this is path    ",path)
        s = path[-1]
        explored.append(s)
        if s==goal: return path
        for neighouber in graph[s]:
            if neighouber not in explored and neighouber not in frontier:
                new_path = list(path)
                new_path.append(neighouber)
                frontier.append(new_path)
                print("this is the second fronter",frontier)
    return "no path found"



print(DFS(graph, "A", "B"))
               
                
                
        
        