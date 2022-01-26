def combine(ori_list):
    out_list = []
    for i in range(len(ori_list)-1):
        if ori_list[i].isalpha() and ori_list[i+1].isalpha() :
            out_list.append(ori_list[i]+ori_list[i+1])
            
    return out_list

def charnum(subject):
    if subject.isnumeric() or subject.isalpha():
        return True
    return False

def addcount(exlist, count,value):
    for i in range(count):
        exlist.append(value)
        
    return exlist

def solution(str1, str2):
    answer = 0
    #원소중복허용하니까 set은 안됨 ascending 등 사용가능 <> 근데 순서는 안 중요함
    
    list1, list2 = list(str1.lower()), list(str2.lower())
    list1, list2 = combine(list1), combine(list2)
        
    numerator,set3 = [], [] #분자용set3
    
    for a in list1:
        if a in list2 and a not in set3:
            if list1.count(a) <= list2.count(a):
                set3 = addcount(set3,list1.count(a),a) #분자는 괜찮음 <> 안괜찮음 
            else:
                set3 = addcount(set3,list2.count(a),a)
    
    denominator = len(list1)+len(list2)-len(set3)
        
    if denominator == 0 : return 65536
    
    return int(65536*(len(set3)/denominator))

