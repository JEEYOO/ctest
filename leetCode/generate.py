class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        listlist = []
        #List[List[int]]
        for i in range(numRows) : 
            tempList = []
            '''
            FIRST & LAST 1
            '''
            
            #1 FIRST 
            tempList.append(1)

            #1 1
            #1 1+1 1
            #1 1+2 2+1 1
            listlist.append(tempList)

        print(listlist)        
            
            

