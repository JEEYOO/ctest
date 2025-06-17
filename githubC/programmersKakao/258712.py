def solution(friends, gifts):
    answer = 0
    
    num = len(friends)
    #n*m
    friends_map = [num * [0] for anyt in range(num)]
    #print(friends_map)
    
    friends_dic = {}
    for i in range(num) : 
        friends_dic[i] = friends[i]
    #print(friends_dic)
    
    """
    for fromTo in range(len(gifts)): 
        #gifts[fromTo].split()[1] 
    """
    for each in range(len(gifts)):
        fromT, toT = gifts[each].split()
        fromKey = friends.index(fromT)
        toKey = friends.index(toT)
        temp = friends_map[fromKey][toKey] 
        friends_map[fromKey][toKey] = temp+1
    print(friends_map)

    jisu1 = dict()
    for i in range(num) :
        jisu1[friends[i]] =  rowSum(friends_map, i)
    
    return answer

def rowSum(map1, b) : #b 가 행
    sumNum = 0
    
    for i in range(len(map1)) : # n * n 모양이니 괜찮
        sumNum += map1[b][i]

    return sumNum
