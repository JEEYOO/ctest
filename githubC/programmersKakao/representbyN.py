
possibleList = []


def arithmetic(N, List) :
    possibleList.append([])
    for i in range(len(possibleList[count-1])):
        if (possibleList[count-1][i]+N) not in possibleList[count-1]:
            possibleList[count].append(possibleList[count-1][i]+N)
        if (possibleList[count-1][i]-N) not in possibleList[count-1]:
            possibleList[count].append(possibleList[count-1][i]-N)
        if (possibleList[count-1][i]*N) not in possibleList[count-1]:
            possibleList[count].append(possibleList[count-1][i]*N)
        if (possibleList[count-1][i]/N) not in possibleList[count-1]:
            possibleList[count].append(possibleList[count-1][i]/N)
            
def solution(N, number):
    count = 0
    possibleList.append([])
    possibleList[count].append(N) 
    if number in possibleList[count]:
        return count+1
    
    while (count<=7) : 
        count = count+1
        #print(count)
        arithmetic(count, N)
        #print(possibleList)
        if number in possibleList[count]: 
            #print(possibleList[count])
            return count+1
    
    return -1
