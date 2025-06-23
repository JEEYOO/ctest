class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        answer : List[int] = []

        for i in sorted(setNums):
            answer.append(int(i))

        
        numbering = 0
        for eachNum in answer:
            nums[numbering] = eachNum
            numbering += 1

        return len(answer)
