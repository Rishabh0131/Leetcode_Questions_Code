from typing import List

class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = 1
        
        k = 1

        if len(nums) == 2:

            if nums[i] == nums[j]:

                return k
            
            return k+1

        while (i < len(nums)) and (j < len(nums)):

            if nums[i] == nums[j]:
                
                j += 1
            
            if j > (len(nums) -1):

                return k
