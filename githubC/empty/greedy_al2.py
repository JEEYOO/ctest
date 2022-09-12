#42883
def cipher(number) :
    #n cipher 
    n=2
    while number != (number % (10**n)) :
        n += 1 
    
    return n 


#converse to list, sort 
def nlist(number, n):
    nlist = []
    x=1
    
    while len(nlist) != n :
        nlist.append(number % 10)
        number = number // 10
        x += 1
    
    nlist.sort()
    return nlist


def solution(number, k):
  
    c = cipher(int(number))     
    n = nlist(int(number), c)
    
    print(n)
    
    answer = ''
    a=0
    #string type return 
    while (a < len(n)-k) :
        answer += str(n[len(n)-a-1])
        a += 1
    
    return answer
