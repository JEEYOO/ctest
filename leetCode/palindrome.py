class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 : return False

        """
        listX = list(str(x))
        listO = listX[::-1]
        """

        if str(x) == str(x)[::-1] :
            return True
        else : return False
