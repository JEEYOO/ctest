class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        theNumber = columnNumber
        
        answer = ''

        alpDic = {'0':'A',  '1':'B',  '2':'C',  '3':'D',  '4':'E',
    '5':'F',  '6':'G',  '7':'H',  '8':'I',  '9':'J',
    '10':'K', '11':'L', '12':'M', '13':'N', '14':'O',
    '15':'P', '16':'Q', '17':'R', '18':'S', '19':'T',
    '20':'U', '21':'V', '22':'W', '23':'X', '24':'Y',
    '25':'Z'}
        
        while (theNumber > 0) : #By the quotient 
            theNumber -= 1 #27 0
            temp = theNumber % 26 #1 
            answer = alpDic[str(temp)] + answer #AB
            theNumber = theNumber // 26 #1
        
        #answer =  alpDic[str(theNumber)]+ answer
        
        return answer
