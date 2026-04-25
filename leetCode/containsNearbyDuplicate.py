def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)) : #0~5
            if nums[i] not in emptySet : 
                emptySet.add(nums[i]) #1 2 3 1 2 3
            else :
                    return True
#               j += 1
#           i += 1
            if len(emptySet) > k : # >3
                emptySet.remove(nums[i-k])    
        
        return False
