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
        fromF, toF = gifts[each].split()
        friends_map[friends_dic[fromF]][friends_dic[toF]] += 1 
    print(friends_map)
    
    return answer
