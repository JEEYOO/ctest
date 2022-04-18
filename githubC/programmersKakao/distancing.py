def distancing(places):
    answer = []
    rooms = len(places)
    
    for i in range(rooms):
        cmap = places[i] #['POOOP', 'OXXOX', 'OPXPX', 'OOXOX', 'POXXP']
        matrix = []
        
        for row in range(5):
            matrix.append([])
            for col in range(5):
                line = cmap[row]
                chars = line[col].split()
                
                #print(chars)
                matrix[row].append(chars)

        answer.append(bfs(matrix))
        
    return answer

def bfs(matrix):
    result = 0 
    for row in range(5):
        for col in range(5):
            #print('test2') is working
            if matrix[row][col] == 'P': #row=3, col=0
                if row+1 <=4 :  
                    result += bfs1(matrix, row+1, col) 
                if col+1 <=4 : 
                    result += bfs2(matrix, row, col+1)
                if row-1 >=0 : 
                    result += bfs3(matrix, row-1, col) 
                if col-1 >=0 : 
                    result += bfs4(matrix, row, col-1)

                #result += num
                #print(count)
    #print(result)
    if result >= 1 : return 0
    else: return 1


def bfs1(matrix, row, col):
    result = 0
    if matrix[row][col] == 'P': return 1
    elif matrix[row][col] == 'X' : return 0
    else :  
        if row+1 <=4 : 
            if matrix[row+1][col] == 'P': return 1
            else : result += 0 
        if col+1 <=4 : 
            if matrix[row][col+1] == 'P': return 1
            else : result += 0
        if col-1 >=0 : 
            if matrix[row][col-1] == 'P': return 1
            else : result += 0         
            
       #elif matrix[row][col] == 'O'
        return result

def bfs2(matrix, row, col):
    result = 0
    if matrix[row][col] == 'P': return 1
    elif matrix[row][col] == 'X' : return 0
    else :  
        if row+1 <=4 : 
            if matrix[row+1][col] == 'P': return 1
            else : result += 0 
        if col+1 <=4 : 
            if matrix[row][col+1] == 'P': return 1
            else : result += 0
        if row-1 >=0 : 
            if matrix[row-1][col] == 'P': return 1
            else : result += 0         
            
       #elif matrix[row][col] == 'O'
        return result 
    
def bfs3(matrix, row, col):
    result = 0
    if matrix[row][col] == 'P': return 1
    elif matrix[row][col] == 'X' : return 0
    else :  
        if col+1 <=4 : 
            if matrix[row][col+1] == 'P': return 1
            else : result += 0
        if row-1 >=0 : 
            if matrix[row-1][col] == 'P': return 1
            else : result += 0         
        if col-1 >=0 : 
            if matrix[row][col-1] == 'P': return 1
            else : result += 0         
            
       #elif matrix[row][col] == 'O'
        return result 
    
def bfs4(matrix, row, col):
    result = 0
    if matrix[row][col] == 'P': return 1
    elif matrix[row][col] == 'X' : return 0
    else :  
        if row+1 <=4 : 
            if matrix[row+1][col] == 'P': return 1
            else : result += 0 
        if row-1 >=0 : 
            if matrix[row-1][col] == 'P': return 1
            else : result += 0         
        if col-1 >=0 : 
            if matrix[row][col-1] == 'P': return 1
            else : result += 0         
            
       #elif matrix[row][col] == 'O'
        return result 
    

'''
print(places[0][0][0])
'''
