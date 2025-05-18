class Solution:
    def convert(self, s: str, numRows: int) -> str:  
        pattern = 2 + (numRows-2) * 2

        answer = ""

        for a in range(numRows-2): #2
            for b in range(numRows-2):
                while a+pattern*b < len(s) :
                    answer += s[a+pattern*b] 

        return answer 
