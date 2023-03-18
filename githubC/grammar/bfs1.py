from collections import deque

def bfs(graph, start, visited): 
    deque1 = deque([start]) #start like 1
    visited[start] = True
    
    while deque1:
        #Pick row at queue
        row = deque1.popleft()
        print(target, end=' ')
        
        for each in graph[row]:
            if not visited[each]:
                deque.append(each)
                visited[each] = Ture
