from typing import List

class Solution:


    def hasDuplicate_hashTable_Solution(self, nums: List[int]) -> bool:
        
        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table.keys():

                hash_table[nums[i]] = 1

            else:

                hash_table[nums[i]] += 1
        

        for key,value in hash_table.items():
            
            if value > 1:

                return True
        
        return False
    
    def hasDuplicate_hashSet_Solution(self, nums: List[int]) -> bool:

        
        hash_set = set()

        for i in range(len(nums)):

            if nums[i] not in hash_set:

                hash_set.add(nums[i])
            
            else:

                return True
            
        
        return False