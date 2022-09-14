def dic(char, num): #num 
    distance = abs( ord(char)-ord(num) )
    if distance > 13 :
        return 26- distance
    else :
        return distance

def solution(name):
    answer = dic(name[0], 'A')
    
    c=1 #counter
    which = dic(name[0])
    while c < len(name) :
        answer += dic(name[c],name[c-1])
        c += 1
    
    return answer
