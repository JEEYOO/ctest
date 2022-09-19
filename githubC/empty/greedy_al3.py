#42860
def dic(char):
    distance = abs( ord(char)-ord('A') )
    if distance > 13 :
        return 26- distance
    else : return distance

def a(char, pointer):
    if len(char)==pointer : return False
    
    for p in range(pointer, len(char)):
        if char[p] != 'A' : return False
    
    return True

def ab(char, pointer): #backward
    if len(char)==pointer : return False

    for p in range(len(char)-1, pointer, -1):
        if char[p] != 'A' : return False
    
    return True

def solution(name):
    answer = dic(name[0]) #first char
    print(answer)
    if a(name, 1): return 0
    
    if name[1]=='A': #reverse
        '''
        immediately return answer if the rests are A
        '''
        p = 1
        c=len(name)-1 #counter
        while c > 0 :
            answer += dic(name[c])
            c -= 1
            p += 1
            if ab(name, c-1) : 
                answer += len(name)-p
                return answer
        answer += len(name)-2 # counting char move   
    else : #orthodromic
        c=1
        while c < len(name) :
            answer += dic(name[c])
            c += 1
            
            if a(name, c) : #c=5
                answer += len(name)-c #5-5
                return answer
        answer += len(name)-1 #counting char move
        
    return answer






def dic2(char, num): #num 
    distance = abs( ord(char)-ord(num) )
    if distance > 13 :
        return 26- distance
    else :
        return distance

def solution2(name):
    answer = dic2(name[0], 'A')
    
    c=1 #counter
    which = dic(name[0])
    while c < len(name) :
        answer += dic2(name[c],name[c-1])
        c += 1
    
    return answer
