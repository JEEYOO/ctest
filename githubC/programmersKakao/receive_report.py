def solution(id_list, report, k):
    answer = []
    point = [] #two list for report and result
    report_dic = {}
    
    for each_id in id_list:
        report_dic[each_id] = 0
    
    for each in report:
        if each.split()[0] in report_dic:
            each.split()[0]
    
    return answer
