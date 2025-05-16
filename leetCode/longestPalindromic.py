class Solution:
    def longestPalindrome(self, s: str) -> str:
        #0~1 characters to itself 
        if len(s) <= 1 : return s
        
        answer = ""
        #ODD
        if len(s) % 2 == 1 :
            answer = s[len(s)//2]
            mid = len(s)//2 
            for i in range(1, len(s)//2): #1AND 3
                if s[mid-i] == s[mid+i] :
                    answer += s[mid-i] #BACK
                    answer = s[mid-i] + answer #FRONT
                else : return answer                                
        #EVEN  
        else : 
            mid1 = len(s)//2 - 1
            mid2 = len(s)//2
            answer = s[mid1:mid2+1]
            for i in range(1, len(s)//2): #1AND 3
                if s[mid1-i] == s[mid2+i] :
                    answer += s[mid1-i] #BACK
                    answer = s[mid1-i] + answer #FRONT 
                else : return answer 

        return answer
