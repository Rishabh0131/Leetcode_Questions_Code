
from typing import List




class Solution(object):
    
    
    def twoSum_bruteForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] + nums[j] == target:

                    return [i,j]

        return []
    

    def twoSum_hashTable(self, nums: List[int], target: int) -> List[int]:
        
        index_hash = {}

        for i, val in enumerate(nums):

            index_hash[val] = i

        
        for i, val in enumerate(nums):

            diff = target - val

            if diff in index_hash and index_hash[diff] != i:

                return [i, index_hash[diff]]

        return []
    