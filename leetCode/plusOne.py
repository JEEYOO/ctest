class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = 1

        # TYPE CASTING TO INTEGER
        for i in range(len(digits)):
            number += digits[i] * (10 ** (len(digits)-1 -i) )
        
        strList = list(str(number))

        return self.strToInt(strList) 

    def strToInt(self, strList: List[str]) -> List[int]:   
        intList = []
        
        for i in strList :
            intList.append(int(i))

        return intList
    
