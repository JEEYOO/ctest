class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = s.split()
        words = len(sList)
        return len(sList[words-1])
