def solution(sizes):
    #가로 30~80
    #세로 30~70 
    
    # print(max(sizes)) 출력값 [w,h] 형식
    
    #가로 세로의 max 중 큰 것은 고정
    maxn = 0
    #side = 'l'
    
    for i in range(len(sizes)):
        if maxn < sizes[i][0] : 
            maxn = sizes[i][0]
          
    for i in range(len(sizes)):
        if maxn < sizes[i][1] : 
            maxn = sizes[i][1]
            #side = 'r'
    
    #그리고 각각 명함에서 가로,세로 중 작은것의 max
    
    #print(sizes[1])    
    #print(min([60,50]))
    
    leastn = 0
    for i in range(len(sizes)):
        if leastn < min(sizes[i]) : 
            leastn = min(sizes[i]) 
    
    
    return maxn*leastn
