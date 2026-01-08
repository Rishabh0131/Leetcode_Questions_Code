from typing import List


class Solution:
    def brute_nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:

        res_stack = []

        for i in range(len(nums1)):

            num1_index_at_num2 = nums2.index(nums1[i])
            if num1_index_at_num2 == len(nums2) - 1:
                res_stack.append(-1)
            else:
                found = 0
                for j in range(num1_index_at_num2, len(nums2)):
                    if nums2[j] > nums2[num1_index_at_num2]:
                        res_stack.append(nums2[j])
                        found = 1
                        break
                if found == 0:
                    res_stack.append(-1)

        return res_stack

    def eff_nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:

        stack = []
        next_greaterMap = {}

        for num in nums2:

            while stack and num > stack[-1]:
                n = stack.pop()
                next_greaterMap[n] = num
            stack.append(num)

        for num in stack:
            next_greaterMap[num] = -1

        return [next_greaterMap[num] for num in nums1]


s = Solution()

print(s.eff_nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
