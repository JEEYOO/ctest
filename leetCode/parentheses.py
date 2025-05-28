class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')

        return not bool(s)
"""        
        dic = {'(':')', '{':'}', '[':']'}
        
        rmList = list(s)
        rmList2 = list(s) #SHALLOW COPY?

        while len(rmList) > 0 :
            #      2
            #      6      
            if rmList[0] in dic :
                #     (
                temp = rmList[0]
                rmList.remove(rmList[0]) #OPEN BRACKET
                
                            #     ( 
                if dic[temp] in rmList:
                    rmList.remove(dic[temp]) #CLOSE BRACKET 
                else : return False    
            else : return False
            #rmList = rmList2 #SHALLOW COPY

        return True        

"""
#listS = list(s) # (, )

while len(rmList) > 0 :
            #      2  
            for i in range(len(s)) : 
            #  0,1             2    
                if listS[i] in dic :
                   #     (
                    rmList.remove(listS[i]) #OPEN BRACKET
                                #     ( 
                    if dic[listS[i]] in rmList:
                        rmList.remove(dic[ listS[i] ]) #CLOSE BRACKET 
                    else : return False    
                else : return False
"""
