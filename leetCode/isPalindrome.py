class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # removing all non-alphanumeric characters
        listS = list(s)

        #print(listS)

        stringF = ""
        for eachChar in listS :
            if "A" <= eachChar <= "Z" :
                stringF += eachChar.lower()
            elif "a" <= eachChar <= "z" or "0" <= eachChar <= "9" :
                stringF += eachChar    

        # BACKWARD COMPARISION
        #print(str(reversed(stringF))

        if  stringF == stringF[::-1] : return True
        else : return False
