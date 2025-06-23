class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for each in range(len(s)//2) :
            temp = s[each]
            s[each] = s[len(s)-1-each] # 6-1-0
            s[len(s)-1-each] = temp
