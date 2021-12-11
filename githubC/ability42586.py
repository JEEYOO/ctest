import math

def solution(progresses, speeds):
    answer = []
    k = [0] * len(progresses) # [0,0,0]
    #print(len(progresses) - 1)
    
    for i in range(len(progresses)):
        # rr = int(math.ceil((100-progresses[i])/speeds[i]))
        rr = (100 - progresses[i]) / speeds[i]  # 0때문에 에러나는거 아니야? 
        if rr > int(rr): # 이건뭐지? 혹시 / 가 몫이 아닌가? 아니네!!
                         # 아니면 이 때 2.0 > 2 면 결과가 뭐냐? false 가아니라면 킹능성 *test해보기 -> 응 아니고 
            rr = math.floor(rr) + 1 #잠만, 반올림인데? 이거 내림해야해 
        k[i] = int(rr)

    cnt = 0
    
    cnt2=1
    while k: # 이건 또 뭐야;; 보니까 복붙했는데도 정답이 안 맞은 거였구나 내가 푼 게 아니라 
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
