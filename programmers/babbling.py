def solution(babbling):
    
    answer = 0
    
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya", "#")
        babbling[i] = babbling[i].replace("ye", "#")
        babbling[i] = babbling[i].replace("woo", "#")
        babbling[i] = babbling[i].replace("ma", "#")
        babbling[i] = babbling[i].replace("#", "")
        
    for i in range(len(babbling)):
        if babbling[i] == "" :
            answer += 1
    
    print(babbling)
    
    return answer

'''
    correct = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in range(len(babbling)):
        if babbling[i-1] in correct :
            answer +=1        
'''
