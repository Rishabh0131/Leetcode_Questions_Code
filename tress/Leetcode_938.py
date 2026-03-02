from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque([root])

        res = 0

        while q:
            node = q.popleft()

            if not node:
                continue
            if node.val >= low and node.val <= high:
                res += node.val

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return res

    def rangeSumBSTOptimal(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBSTOptimal(root.right, low, high)

        if root.val > high:
            return self.rangeSumBSTOptimal(root.left, low, high)

        return (
            root.val
            + self.rangeSumBSTOptimal(root.left, low, high)
            + self.rangeSumBSTOptimal(root.right, low, high)
        )
