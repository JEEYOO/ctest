def round3(number):
    return math.floor(number*1000)/1000.0

def startp(line):
    #1차 나누기 띄어쓰기
    each = line.split()
    
    #1.1 - 날짜가 쓸모가있나? ㄴㄴ 9월 15일이라고 못박아놓음
    
    #1.2 :만 있는게아니네;; 아니면 소수점으로 계산하던가     타입은 float 으로하면되겠고
    time = each[1].split(':')

    #1.3 s를 어떻게 떼지 --검색 및 시행착오--> each[:-1]   타입은 float( ) 등으로 가능
    #-로 뚫어버리면... 뭐 그떈 위에서 뺴면되겠지
    minus = float(each[2][:-1])
    
    #시작점찾기 s에 붙어있는거 -하면되겠네
    hours = int(time[0])
    minutes = int(time[1])
    seconds = float(time[2])-minus+0.001 #아 이거 너무 임시방편인데 +0.002
    
    return hours*3600 + minutes*60 + seconds #round로도 에러있음


def endp(line) : #아 그냥 초로 계산해주는 거를 만드는 게 낫겟는데 이미 했으니까 그냥 해야겠다
    #1차 나누기 띄어쓰기
    each = line.split()
    
    #1.1 - 날짜가 쓸모가있나? ㄴㄴ 9월 15일이라고 못박아놓음
    
    #1.2 :만 있는게아니네;; 아니면 소수점으로 계산하던가     타입은 float 으로하면되겠고
    time = each[1].split(':')

    #시작점찾기 s에 붙어있는거 -하면되겠네
    hours = int(time[0])
    minutes = int(time[1])
    seconds = float(time[2]) #아 float 여서 그렇구나 ㅅㅂ
    
    return hours*3600 + minutes*60 + seconds #round는 실패


def solution(lines):
    answer = 0
    
    '''
    -네.포함해서
    결국 1초안에 최대한 들어오는 것(시작포인트도 맘대로임)
    '''
    #dic = {}
    arrayList = []
    for num in range(len(lines)):
        start = startp(lines[num])
        end = endp(lines[num])
        '''
        나누기는 이제 되었으니까 방법이 문제네
        
        .
        일단 각 라인별로 점 2개가 생긴다고 생각하면 됨
        어차피 최대만 찾기 때문에 점'만' 보면 된다. 
        [a,b,c,d...] 이라고 볼 때
        a 의 시작점, 끝점 이 나머지 b,c,d... 의 시작점 끝점에 들어가는가 를 보면 되겠네  
        '''''' 의 위치도 영향을 미치는 구나
        '''
        arrayList.append(start) #+1으로도 안되고, *2로도 안되고 차라리 array로 할까 
        arrayList.append(end) #뒤에만 들어가는거알면되는거같은데 
        
        '''
        아 그러고보니 판단할 때 앞의 점보다 큰지 적은지만 판단하면 되네 <> A가 뒤에있을지라도 end 가 크면 그 뒤에서도 커버가 가능
        A.            .
        B  .           .
        C    .          .
        그렇게 보면 A는 절대아니겠구만

        그냥 시작점 계산해주는 함수를 하나 만드는 것이 낫겠는데
        
        오답풀이 생각해보니 전부 초단위로 만들었던거같음. 시간은 3600 곱하고, 분은 60만 곱하면되니
        '''   
        
    '''
    잠만 근데 각각을 어떻게 호출하지. numbering 으로가능한가 Python Shell 에서 테스트 先 -> 안되네
    그럼 그냥 홀수짝수로 할까 
    '''
    result = [] #결과 하나씩 추가. 아 근데 어차피 제일 최고만 올리면 되니까 이렇게 안해도되긴해. int update 식으로 해도되고
    for total in range(len(arrayList)):
        #total은 필요하다. 중심을 딱 잡아주기 위해
        count=0
        eachp = arrayList[total] #이래야 시작점만 포인트가능 <> 끝점도 필요한데?  
        #end = arrayList[total*2+1]
        
        for i in range(len(lines)): #일단 홀짝테스트
            
            #eachp+0.999 #얘가문제 3603.0009999999997
            
            if  (arrayList[2*i] <= round(eachp,3) and round(eachp,3) <= arrayList[2*i+1]) or (arrayList[2*i] <= round(eachp+0.999,3) and round(eachp+0.999,3) <= arrayList[2*i+1]) :
                
                 #맞네 처음이안되네!
                count=count+1
                
            '''지금 쟁점은 Test 4 
            3604.002가 eachp이고
            i가 1일 때 
            3605.001에서 왜 같다교 count up이 안되는거지
            '''
            #((end >= arrayList[2i]) and (end <= arrayList[2i+1])) +0.999
            #(arrayList[2*i] <= start-1 and start-1 <= arrayList[2*i+1])
                
        #본인은 빼야지 -1 <> 할필요없음
        result.append(count)
    # 아;;;;;;;;; count 하는 로직을 잘못알았다. 그럼 거의 처음부터다시짜야하는거아닌가 ㄷㄷ <> 아 아니지 어차피 첫점 끝점 +-1만 하면 같음 ㅇㅋㅇㅋ ㄱㄱ
    
    
    
    
    answer = max(result)
    if answer == 0:
        return 1
    return max(result)






'''
float(format(eachp+0.999,".3f")) 

얘들은 뭐 테스트도 통과못함
def truncate(num, n): 
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def truncate2(num,n):
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+n+1])
            except:
                return float(temp)      
    return float(temp)
'''


"""
'''
    근데 이거 문제가... 결국 count를 해야하는데 앞 뒤 전부 가능해야함. dictionary로해야하나? 그럼 for 할때부터 dictionary 만들어놔야할듯  
    '''
    

    for counting in range(len(arrayList)):
        
        result[counting] = arrayList[counting]
        print(result)
        if len(result) == len(arrayList):
            break
"""


"""
방법2
    #-가 되면 60에서 빼서 반영
    if seconds < 0 :
        if minutes==0: #1분만있어도 커버 가능하니
            #소수점 아닌이상 int가 낫겠다
            hours = hours -1
            minutes = 59
        else:
            minutes = minutes-1
            seconds = 60 + seconds
         #분이 00 일떄랑 케이스 나눠서 시간 -1할지안할지 판단하고.. 

    return hours +':' + minutes + ':' + seconds#이렇게 해버리면 얘가 계산을 못하잖아 아 할수는 있나 ㄴㄴ <> unsupported operand type(s) for +: 'int' and 'str' 
"""

'''
방법1
각 소숫점에 1을 추가하는 방식은 너무 무식한데 
ex) 20:59:57.421   0.351s  이면
        
    20:59:57.419   +1
    20:59:57.420   +1
    20:59:57.421   +1
'''
