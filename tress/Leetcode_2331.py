from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val in (2, 3):
                if node.val == 2:
                    return left or right
                else:
                    return left and right

            else:
                return False if not node.val else True

        return dfs(root)
