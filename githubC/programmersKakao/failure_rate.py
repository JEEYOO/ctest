import copy

def solution(N, stages):
    result = []
    #N=5 의 예시는 이해했는데
    #N=4일 때 왜 4321도 아니고 4123이지 -> 실패율이 높은 스테이지부터 내림차순으로
    
    dic = {}
    for init in range(N+2): # N보다 더 큰 값이 있을수있음 
        dic[init] = 0
    
    print(dic)
    for i in range(len(stages)):
        dic[stages[i]] = dic[stages[i]] +1
    print(dic)
    
    denomitor = len(stages)
    dic2 = copy.deepcopy(dic)
    for k in range(1,len(dic)):
        denomitor = denomitor-dic2[k-1]
        if denomitor != 0 :
            dic[k] = dic2[k] / denomitor #지워야하는데 
            
    print(dic)
    while(len(result)!=N):
        save, maximum = N,0
        for n in range(1,N+1): #거꾸로가야함
            if dic[n] > maximum:
                maximum = dic[n]
                save = n
        if dic[save] != -1:            
            result.append(save)
            dic[save] = -1
        else:
            for n in range(1,N+1):
                if dic[n]==0:
                    result.append(n)
                    dic[n] = -1
                    break
    print(dic)
    return result
