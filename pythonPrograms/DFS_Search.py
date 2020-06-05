graph = {'A': ['Z', 'S', 'T'],
         'T': ['A','L'],
         'L': ['T', 'M'],
         'M': ['L','D'],
         'D': ['M', 'C'],
         'C': ['P','R','C'],
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
visited=[]


def dfs(visited, graph, node ,goal):
   
    if node not in visited:
        visited.append(node)
        if visited[-1]== goal:
            print(visited)
       
         
        
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, goal)
       



dfs(visited, graph, "A" , "V")

