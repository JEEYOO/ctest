def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)) : #0~5
            for j in range(i+1,len(nums)) : #1~5
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
#               j += 1
#           i += 1

        return False
