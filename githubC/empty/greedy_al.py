#42885
def solution(people, limit):
    answer = 0
    
    people.sort()
    #print(people)
    x = 0 
    y = len(people)-1
    #temp = 0
    
    while(x<y) : 
        answer += 1
        if people[x] + people[y] > limit : pass
        else : x += 1 
        y -= 1
        if x==y : answer += 1
        
    return answer
