
possibleList = []

def NN(N, times) :
    result = 0
    for a in range(times):
        each = N
        for b in range(a):
            each = each * 10
        result += each
    return result

def arithmetic(list1, list2, count) :
    j= len(list1)
    k= len(list2)
    
    for a in range(j):
        for b in range(k):
            if (list1[a]+list2[b]) not in possibleList[count]:
                possibleList[count].append(list1[a]+list2[b])
            if (list1[a]-list2[b]) not in possibleList[count]:
                possibleList[count].append(list1[a]-list2[b])
            if (list1[a]*list2[b]) not in possibleList[count]:
                possibleList[count].append(list1[a]*list2[b])
            if (list2[b]!=0) : 
                if (list1[a]/list2[b]) not in possibleList[count]:
                    possibleList[count].append(list1[a]/list2[b])
            
def solution(N, number):
    possibleList.append([]) #그냥 0은 empty하게 두자 
    
    count = 1
    if number == N : return count #N이면 그냥 1 제출하라는거지
    
    possibleList.append([])
    possibleList[count].append(N) #[ [], [5] ]
    # print(possibleList) 맞는데
    while count <= 8:
        count=count+1
        possibleList.append([])
        possibleList[count].append(NN(N, count)) #55 추가  
        for i in range(1,count): 
            #if (count-i) >= i:
            arithmetic(possibleList[i], possibleList[count-i],count)
            if number in possibleList[count]: 
            #print(possibleList[count])
            return count
    
    return -1
