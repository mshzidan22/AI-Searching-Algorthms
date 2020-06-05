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

#Bridth first search
def BFS_Search(graph, start, goal):

 explored = []  
 queue = [[start]]
 if start == goal:
    return "this is the goal"
 while queue:
    path =queue.pop(0)
    node=path[-1]
    if node not in explored:
        neighbours=graph[node]
        for n in neighbours:
            new_path = list(path)
            new_path.append(n)
            queue.append(new_path)
            if n == goal:
                return new_path
        explored.append(node)
         
return "sorry no path is avilable"           
            
        
 



 
print(BFS_Search(graph, "A" ,"B"))    