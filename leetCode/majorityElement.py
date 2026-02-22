class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}

        for each in nums : 
            if each in dic :
                dic[each] += 1 
            else :
                dic[each] = 1

        #print(dic)

        maxV = max(dic.values())
        
        #print(maxV)
        
        for each2 in dic : 
            if dic[each2] == maxV :
                answer = each2
        
        return answer
