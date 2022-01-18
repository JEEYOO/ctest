def combine(ori_list):
    out_list = []
    for i in range(len(ori_list)-1):
        if (charnum(ori_list[i]) and charnum(ori_list[i+1])) :
            if not (ori_list[i]+ori_list[i+1]).isnumeric():
                out_list.append(ori_list[i]+ori_list[i+1])
    return out_list

def charnum(subject):
    if subject.isnumeric() or subject.isalpha():
        return True
    return False

def solution(str1, str2):
    answer = 0
    #원소중복허용하니까 set은 안됨 ascending 등 사용가능 <> 근데 순서는 안 중요함
    
    list1, list2 = list(str1.lower()), list(str2.lower())
    list1, list2 = combine(list1), combine(list2)
        
    numerator,set3 = set(), set() #분자용set3
    
    for a in list1:
        numerator.add(a)
        if a in list2:
            set3.add(a)
    for b in list2:
        numerator.add(b)
        
    if len(numerator) == 0 : return 65536
    
    return int(65536*(len(set3)/len(numerator)))

'''
list.sort() = none
sorted(list1,reverse=True)
'''
