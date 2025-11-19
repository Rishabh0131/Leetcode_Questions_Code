from typing import List

class Solution:

    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        
        count_hash = {}


        for i in range(len(nums)):

            count_hash[nums[i]] = 1 + count_hash.get(nums[i], 0)
        
        sorted_pairs = []
        
        for key, value in count_hash.items():
            
            sorted_pairs.append([value, key])
                
        sorted_pairs.sort()

        res  = []
        
        for i in range(0,k):
            
            res.append(sorted_pairs.pop()[1])
            

        return res
    
    def topKFrequent_bucketSort(self, nums: List[int], k: int) -> List[int]:
        
        count_hash = {}

        for i in range(len(nums)):

            count_hash[nums[i]] = 1 + count_hash.get(nums[i], 0)

        mapped_arr = [[] for i in range(len(nums) + 1)]


        for num, cnt in count_hash.items():
            mapped_arr[cnt].append(num)
        
        res = []
        for i in range(len(mapped_arr)-1, -1 , -1):
            for num in mapped_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res