def dic(char): #num 
    if ord(char) < 79 :
        joyst = ord(char) - 65
    else :
        joyst = ord(char) - 91  
    return joyst

def solution(name):
    answer = dic(name[0])
    
    c=1 #counter
    which = dic(name[0])
    while c < len(name) :
        answer += abs(which - dic(name[c])) 
        which = dic(name[c])
        #dic(name[p], dic(name[p-1], 0) ) #0 is wrong
        c += 1
    
    return answer
