class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        answer = 0
        alphabets = list(columnTitle)
        length = len(alphabets)-1
        
        for each in alphabets :                         #
            answer += (ord(each)-64)* (26**length)      # (65-64) * (26**1)  A
                                                        # (66-64) * 26* the power of 0 =1
            length -= 1                         

        return answer
