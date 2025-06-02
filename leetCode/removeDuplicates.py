class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        answer : List[int] = []

        for i in setNums:
            answer.append(int(i))


        for i in range (1, len(nums)):
            for j in range (i+1, len(nums)): #2 -> indexOut 
                 if nums[i] != nums[j] and nums[i] < nums[j]  : #and nums[i-1]+1 == nums[j]
                    nums[i] = nums[j]
                    break

        return len(answer)
