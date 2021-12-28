


def NN(N, times) :
    result = 0
    for a in range(times):
        each = N
        for b in range(a):
            each = each * 10
        result += each
    return result

def arithmetic(possibleListset, set1, set2, count,N) :
    j= len(set1)
    k= len(set2)
    
    for c in set1:
        for d in set2:
            possibleListset.add(c+d)
            possibleListset.add(c-d)
            possibleListset.add(c*d)
            if (d!=0) : 
                possibleListset.add(c//d)
    return possibleListset
            
def solution(N, number):
    possibleList = []
    possibleList.append(set())  #그냥 0은 empty하게 두자 
    
    count = 1
    if number == N : return count #N이면 그냥 1 제출하라는거지
    
    possibleList.append(set())
    possibleList[count].add(N) #[ [], [5] ]
    # print(possibleList) 맞는데
    while count < 8:
        count=count+1
        possibleList.append(set()) # [ (), (5), (55,7897987) ]
        possibleList[count].add(NN(N, count))
        for i in range(1,count): #1,3
            #if (count-i) >= i:              #1과 2       2와1
            possibleList[count] = arithmetic(possibleList[count], possibleList[i], possibleList[count-i],count,N)
    
    return -1
