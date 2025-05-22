class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        pattern = 2 + (numRows-2) * 2

        answer = ""

        for row in range(numRows):
            i = row
            while i < len(s):
                answer += s[i]
                # Downward / Upward (except for first point and last) 
                if 0 < row < numRows - 1:
                    diag = i + pattern - 2 * row
                    if diag < len(s):
                        answer += s[diag]
                i += pattern 

        return answer 
