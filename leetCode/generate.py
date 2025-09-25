class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        listlist = [[1]]
        if numRows == 1 : return listlist
            
        for each in range(numRows-1) : 
            tempList = []
            tempList.append(1) #FIRST1
            
            for i in range(each) :
           #   0,1           2
                prev_list = listlist[each] #1 1+1 1 PREVIOUS LIST RATHER THAN TEMPLIST 
               #                      2
                
                tempList.append(prev_list[i] + prev_list[i+1])

            tempList.append(1) #LAST1
            
            listlist.append(tempList)

        return listlist        
            
            

