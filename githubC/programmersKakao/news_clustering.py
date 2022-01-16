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
        
    numerator = set()
    denominator = set()
    for a in list1:
        denominator.add(a)
    for b in list2:
        denominator.add(b)
    
    for k in range(len(list1)): #더 짧은 list로 해야
        if list1[k] in list2: #set으로해야겠는데 
            numerator.add(list1[k])
    print(denominator)            
    if len(numerator) == len(list1) : return 65536
    
    return int(65536*(len(numerator)/len(denominator)))

'''
list.sort() = none
sorted(list1,reverse=True)
'''
