#42885
def solution(people, limit):
    answer = 0
    
    people.sort()
    #print(people)
    i = 0 # pointer
    temp = 0
    
    while(i<len(people)) : 
        temp += people[i]
        if temp > limit :
            temp = 0
            answer += 1
        else : i += 1 
        
        if i == len(people) : answer += 1
        
    return answer
