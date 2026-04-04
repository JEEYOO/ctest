def isHappy(self, n: int) -> bool:
        
        #strN = str(n)
        #print(list(strN))
        listN = list(str(n))
        records = set()
        
        while n != 1 and n not in records : # len(listN) != 1  : #1 and int(listN[0])**2 > 10
            records.add(n)
            ckNum = 0
            
            for each in listN : #1,0
                ckNum += int(each)**2

            listN = list(str(ckNum)) 

            n = ckNum
        
        if n == 1:
            return True
        else : return False


        '''
        while True : 
            if (n / 10 != 0) : 
                tempNum += (n / 10)**2
                n = 
            else : 
                tempNum += (n % 10)**2
        '''
