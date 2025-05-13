class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Minimum Length
        minLen = 200
        for i in range(len(strs)) :
            if minLen > len(strs[i]) : 
                minLen = len(strs[i])  

       #answer = 0
        answer = ''
        for t in range(minLen) : # 4
            for i in range(len(strs)-1) : # 3
                if strs[i][t] == strs[i+1][t] : pass    
                else : return answer
            answer += strs[i][t]
        return answer
        
