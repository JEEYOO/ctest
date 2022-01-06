#4.5시간 22.01.04


def substitute(matrix, square):
    a,b,c,d = square[0]-1,square[1]-1,square[2]-1,square[3]-1
    #x-1
    for e in range(d-b): #0~95  이 맥시멈이고96=97-1
        matrix[b+e+1][a] = matrix[b+e][a]
            # 0+e+1   0           0 e  0  
    #y-1
    for w in range(c-a): #0~99-0=99
        matrix[d][a+1+w] = matrix[d][a+w]
              #96 0+1+w           96 0+w
    #x+1
    for q in range(d-b):
        matrix[b+q][c] = matrix[b+1+q][c]
        
    #y+1
    for r in range(c-a):
        matrix[b][a+r] = matrix[b][a+1+r]        
        
    return matrix

def minimum(matrix, square, row, column): #numberset 넣어서 최소값만 반환
    numbers = set()
    a,b,c,d = square[0]-1,square[1]-1,square[2]-1,square[3]-1
    
    for e in range(d-b):
        numbers.add(matrix[b+e][a])
        
    #y-1
    for w in range(c-a):
        numbers.add(matrix[d][a+1+w])
        
    #x+1
    for q in range(d-b):
        numbers.add(matrix[b+q][c])
        
    #y+1
    for r in range(c-a):
        numbers.add(matrix[b][a+r])
    
        
    #리스트면 살짝 다르긴함 i range(len) 써야할듯
    return min(numbers)

def solution(rows, columns, queries):
    answer= []
    
    #일단 그려야
    matrix = [[0]*rows for i in range(columns)]
    for a in range(columns):
        for b in range(rows):
            matrix[a][b] = (b+1) + rows*a
    #0,0인데 값은 1이어야하니

    for square_num in range(len(queries)):
        matrix = substitute(matrix, queries[square_num]) #업데이트
        
        answer.append(minimum(matrix, queries[square_num], rows, columns))
    
    return answer


'''
    일단 return 값이 돌아간 애들 중 최소값이기에 그 테두리만 알면됨, 그것역시 같은 위치인지 if로 파악하고 return 하면됨
    <>본래자리 찾아갔으면
    예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다. -> 이거 때문에 파악이 힘듬. 매번새로그려야하나?
    
    #for side in range(4):
        each_query = numberset(queries[square])
        def numberset(vertexes) #아님 여기서바로 minimum만 배출
    vertexes[0], vertexes[1], vertexes[3], vertexes[4]
    
    #for side in range(4):
    '''
