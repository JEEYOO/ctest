def solution(s):
    answer = 0
    copys = s
    #dictionary 使う方が効率的だと思うけど 아니다 대응을 문자를 먼저해야겠네<> でもarrayで解ける。順番同じだし
    dic2 = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for i in range(len(dic)):
        if dic2[i] in s:
        #print(dic2[i])
        #print(str(dic[dic2[i]]))
            copys = copys.replace(dic2[i],str(dic[dic2[i]])) #print로 체크해보니까 바뀌네! 정답은어떻게 저장할까이군
        
    
    #参考に、今数は文字にする方を
    
    return int(copys)
