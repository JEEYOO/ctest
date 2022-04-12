def solution(id_list, report, k):
    answer = []
    point = [] #two list for report and result
    report_dic = {}
    
    for each_id in id_list:
        report_dic[each_id] = 0
    
    copy_dic = report_dic.copy() #doesn't work without 'copy'
    dist_report = set(report)
    
    for each in report:
        if each.split()[1] in report_dic:
            report_dic[each.split()[1]] += 1
    
    for num in report_dic:
        if report_dic[num] >= k:
            point.append(num)
    
    for each in dist_report:
        if each.split()[1] in point:
            copy_dic[each.split()[0]] += 1
    
    #print(copy_dic)
    
    for i in id_list:
        answer.append(copy_dic[i])
    
    return answer
