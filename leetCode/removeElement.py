class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        fixed = 0 ##
        for i in range(len(nums)):
            if nums[i] != val:
                nums[fixed] = nums[i]
                fixed += 1 ## fill the front values only

        for delete in range(fixed, len(nums)):
            nums[delete] = None

        return fixed
