
def dfs(graph, v, visited):
  #Current node visited.
  visited[v] = True
  print(v, end=' ') # Print the order of visited node
  
  #recursive
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      
visited = [False] * 9

dfs(graph, 1, visited)
