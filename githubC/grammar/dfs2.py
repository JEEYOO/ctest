
graph1 = dict()

graph1[1] = [2,3]
graph1[2] = [1,4]
graph1[3] = [1, 7, 8, 9]
graph1[4] = [2, 5, 6]
graph1[5] = [4]
graph1[6] = [4]
graph1[7] = [3]
graph1[8] = [3]
graph1[9] = [3, 10]
graph1[10] = [9]

#########################

def dfs(graph, start_node):
  
  need_visited, visited = list(), list()
  
  need_visited.append(start_node)
  
  while need_visited:
    
    last_node  = need_visited.pop()
    
    if last_node not in visited:
      visited.append(last_node)
      need_visited.extend(graph1[last_node])
      
  return visited
