#42883

ef maxnum(list1) :
    maxnumber = list1[1]
    for i in range(1,len(list1)):
        if maxnumber < list1[i] : maxnumber = list1[i]
            
    return maxnumber

def where(target, list2):
    for i in range(len(list2)):
        if list2[i] == target:
            return i

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
