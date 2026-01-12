from typing import List

class Solution:


    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:

                low = mid + 1
            
            if nums[mid] > target:

                high = mid - 1

        return low
    
    
    def searchInsertUsingForLoops(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:

            return 0

        for i in range(len(nums)):

            if nums[i] == target:
                return i

            if nums[len(nums) - 1] < target:
                return len(nums) 

            if nums[i] < target and nums[i+1] > target:

                return i+1
