def solution(N, stages):
    answer = []
    #N=5 의 예시는 이해했는데
    #N=4일 때 왜 4321도 아니고 4123이지 -> 실패율이 높은 스테이지부터 내림차순으로
    dic = {}
    for init in range(N+1):
        dic[init] = 0
    print(dic)
    for i in range(len(stages)):
        dic[stages[i]-1] = dic[stages[i]-1] +1
    
    print(dic)
    return answer
