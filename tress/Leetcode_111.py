from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepthRecursive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                q.append([node.left, depth + 1])  # type: ignore

            if node.right:
                q.append([node.right, depth + 1])  # type: ignore

        return 0
