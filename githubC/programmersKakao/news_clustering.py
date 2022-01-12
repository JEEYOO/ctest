def solution(str1, str2):
    answer = 0
    #원소중복허용하니까 set은 안됨 ascending 등 사용가능 <> 근데 순서는 안 중요함
    
    list1, list2 = list(str1), list(str2)
    print(list1) # sorted(list(str1)) Test 4 오류
    print(list2)
    print('e'=='E') #case sensative
    
    return answer

'''
list.sort() = none
sorted(list1,reverse=True)
'''
