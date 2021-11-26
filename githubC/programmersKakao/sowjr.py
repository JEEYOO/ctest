def solution(a, b):
    answer = 0
    
    for v in range(len(a)):
        answer += a[v]*b[v]
    
    return answer
