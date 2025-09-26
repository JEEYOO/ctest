class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for num in nums :
            which = nums.index(num) #which 
            if num not in nums[which+1:] :  
                return num
