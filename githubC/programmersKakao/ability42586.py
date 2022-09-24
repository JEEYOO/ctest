import math

def solution(progresses, speeds):
    answer = []
    k = [0] * len(progresses) # [0,0,0]
    #print(len(progresses) - 1)
    
    for i in range(len(progresses)):
        # rr = int(math.ceil((100-progresses[i])/speeds[i]))
        rr = (100 - progresses[i]) / speeds[i]  # 0 
        if rr > int(rr): #  / remainder 
                         # 2.0 > 2 
            rr = math.floor(rr) + 1 #floor not rounds 
        k[i] = int(rr)

    cnt = 0
    
    cnt2=1
    while k: 
        ddd = len(k)
        # cnt2=1
        r2 = k[cnt]
        for i in range(cnt+1, len(k)):
            paa = (r2, k[i])
            if r2 >= k[i]:
                cnt2 += 1
                cnt+=1
            else:
                cnt +=1
                answer.append(cnt2)
                cnt2 =1
                break
        if r2 == k[len(k)-1]:
            answer.append(cnt2)
            break
    # answer.append(cnt2)
    return answer
