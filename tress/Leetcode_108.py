from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def genBST(L, R):

            if L > R:
                return None

            m = L + (R - L) // 2
            node = TreeNode(nums[m])
            node.left = genBST(L, m - 1)
            node.right = genBST(m + 1, R)

            return node

        return genBST(0, len(nums) - 1)
