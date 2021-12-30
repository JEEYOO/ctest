def numberset(vertexes) #아님 여기서바로 minimum만 배출
    vertexes[0], vertexes[1], vertexes[3], vertexes[4]
    
def minimum(listset, row, column): #numberset 넣어서 최소값만 반환
    maximum = row*column
    for value in listset:
        if value < maximum:
            maximum = value
    #리스트면 살짝 다르긴함 i range(len) 써야할듯
    return maximum

def solution(rows, columns, queries):
    answer = []
    
    for squares in range(len(queries)):
        #for side in range(4):
        each_query = numberset(queries[square])
        answer.append(minimum(each_query, rows, columns))
    return answer
