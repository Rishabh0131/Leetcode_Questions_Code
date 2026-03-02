from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if not root1 and not root2:
            return

        node = TreeNode(
            (0 if not root1 else root1.val) + (0 if not root2 else root2.val)
        )
        node.left = self.mergeTrees(
            None if not root1 else root1.left,
            None if not root2 else root2.left,
        )
        node.right = self.mergeTrees(
            None if not root1 else root1.right,
            None if not root2 else root2.right,
        )

        return node

    def mergeTreesOptimal(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if not root1:
            return root2

        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTreesOptimal(root1.left, root2.left)
        root1.right = self.mergeTreesOptimal(root1.right, root2.right)

        return root1
