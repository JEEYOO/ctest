def solution(lines):
    answer = 0
    
    
    for num in range(len(lines)):
    
        each = lines[num].split()
        time = each[1].split(':')
    
        minus = float(each[2][:-1])
        seconds = float(time[2])-minus 
        
        if seconds < 0 :
        
    return answer
