from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visited = [False]
        res = []

        while stack:
            curr, vist = stack.pop(), visited.pop()

            if curr:
                if vist:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)

        return res

    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def postOrder(node):

            if node is None:
                return

            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)

        postOrder(root)

        return res
