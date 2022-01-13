def combine(ori_list):
    out_list = []
    if (len(ori_list)%2==0): #짝수라면
        for i in range(len(ori_list)/2): #예를들어 4라면 2까지 
            out_list.append(ori_list[2i]+ori_list[2i+1])
    else:
        for i in range(int(len(ori_list)/2)): #예를들어 3라면 1까지 
            out_list.append(ori_list[2i]+ori_list[2i+1])
    return out_list

def solution(str1, str2):
    answer = 0
    #원소중복허용하니까 set은 안됨 ascending 등 사용가능 <> 근데 순서는 안 중요함
    
    list1, list2 = list(str1.lower()), list(str2.lower())
    print(list1) # sorted(list(str1)) Test 4 오류
    print(list2)
    print('e'=='E') #case sensative
    
    return answer

'''
list.sort() = none
sorted(list1,reverse=True)
'''
