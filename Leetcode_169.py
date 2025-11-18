from typing import List

class Solution:

    def majorityElement_HashTable(self, nums: List[int]) -> int:
        
        if len(nums) == 0:

            return 0

        counts = {}

        for i in range(len(nums)):

            if nums[i] in counts.keys():

                counts[nums[i]] += 1
            
            else:
                counts[nums[i]] = 1

        
        for key, value in counts.items():

            if value > (len(nums)/2):

                return key

        return 0
    
    def majorityElement_HashTable_Optimized(self, nums: List[int]) -> int:
        
        if len(nums) == 0:

            return 0

        counts = {}

        for i in range(len(nums)):

            counts[nums[i]] = 1 + counts.get(nums[i], 0)
            if counts[nums[i]] > (len(nums)/2):
                return nums[i]

        return 0

    
    def majorityElement_Optimized(self, nums: List[int]) -> int:
        
        if len(nums) == 0:

            return 0

        res = maj_count = 0

        for i in range(len(nums)):

            if maj_count == 0:

                res = nums[i] 

            if nums[i] == res:
                maj_count += 1
            else:
                maj_count -= 1 

        return res