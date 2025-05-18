class Solution:
    def longestPalindrome(self, s: str) -> str:
        #0~1 characters to itself 
        if len(s) <= 1 : return s
        
        answer = ""
        
        for mid in range(len(s)):
            # ODD PALINDROMIC
            left, right = mid, mid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(answer):
                    answer = s[left:right+1]
                left -= 1
                right += 1

            # EVEM PALINDROMIC
            left, right = mid, mid + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(answer):
                    answer = s[left:right+1]
                left -= 1
                right += 1

        return answer
