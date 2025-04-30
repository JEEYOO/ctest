class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        slist = list(s)   #리스트화
        slen = len(slist) #길이    
        ranswer = 0 

        for i in range(slen):
            current_len = self.lengthOfLongestSubstring2(s[i:])
            if ranswer < current_len :
                ranswer = current_len
                if ranswer >= slen - i:
                    break
        return ranswer

    def lengthOfLongestSubstring2(self, s: str) -> int:    
        count, answer = 0, 0 #잠시 넣을 count 와 count 중 최대값 뽑는 answer
        slist = list(s)   #리스트화
        slen = len(slist) #길이
        nlist = []    

        #빠른 케이스. 단품 or 중복 없을 때 
        if slen == len(set(s)) : return slen 

        #i와 i+1을 비교하여 같다면 거기서 +1 후 중지(초기화 후 그 다음으로 넘어가기)
        for i in range(slen-1):
            if slist[i] == slist[i+1] :
                count += 1
                nlist.append(slist[i])

                if count > answer : answer = count
                count = 0
                nlist = [] 

        #i와 i+1을 비교하여 다르다면
            #case1 :  i+1이 nlist안에 없을경우(마지막?)
            elif slist[i+1] not in nlist and i+1 == slen-1 : 
                count += 2

                if count > answer : answer = count
                return answer                     
            #case2 : i+1이 nlist안에 있을경우 + 새시작
            elif slist[i+1] in nlist :
                count += 1
                nlist.append(slist[i])

                if count > answer : answer = count
                count = 1
                nlist = list(slist[i])
            else : 
                count += 1
                nlist.append(slist[i])

                if count > answer : answer = count

        return answer
"""
        #set 도 못쓰는게 연속되어야하니까 
        for i in range(slen-1):
            if slist[i] != slist[i+1]  : 
                if slist[i] not in nlist : 
                    count += 1
                    nlist.append(slist[i])
                    if i+1 == slen-1 and  slist[i+1] not in nlist : 
                        count+=1
                else : 
                    if i+1 == slen-1 and  slist[i+1] not in nlist : 
                        count+=1
                    if count > answer : answer = count
                    count = 0
                    nlist = []   
                
            else:
                count +=1
                if count > answer : answer = count

                #초기화 
                count = 0
                nlist = []    

        if count > answer : answer = count

        
        if answer == 0 : 
            return 1
        
        return answer
"""
