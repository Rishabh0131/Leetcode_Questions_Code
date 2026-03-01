from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, L, R):

        if not L and not R:
            return True

        if not L or not R:
            return False

        if L.val != R.val:
            return False

        return self.isMirror(L.left, R.right) and self.isMirror(L.right, R.left)
