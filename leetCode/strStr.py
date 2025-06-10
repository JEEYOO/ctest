class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        answer = 0
        compare = ''

        for h in range(len(haystack)):
        #   0               9
            compare = ''
            
            for n in range(len(needle)):
            #   0               3   
                if h+n < len(haystack) :
                    if needle[n] == haystack[h+n]:
                    #        0               0+0   
                        compare = compare + haystack[h+n]
                    else : break

            if compare == needle :
                return h+n - len(needle) + 1    

        if answer == 0:
            return -1
        else : return answer

"""
elif len(compare) >= len(needle) :
                
                    count += 1
                else : break 

                if count == len(needle):
                    count = 0
                    answer += 1

compare = compare + haystack[h] 
        #   issi
            for c in range(len(compare)):
                if needle[c] != compare[c]:
                    compare = '' 

            if compare == needle :
                return h - len(needle) + 1                    
"""
