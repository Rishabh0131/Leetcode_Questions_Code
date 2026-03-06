from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        arr = []

        def dfs(node):

            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)

        res = arr[1] - arr[0]

        for i in range(2, len(arr)):
            res = min(res, arr[i] - arr[i - 1])

        return res
