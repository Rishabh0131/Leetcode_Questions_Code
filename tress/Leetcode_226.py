from collections import deque
from typing import Optional


# Definition for a binary tree root.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root

    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTreeRecursive(root.left)
        self.invertTreeRecursive(root.right)

        return root

    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root
