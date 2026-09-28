# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root, maxVal):
            if root is None:
                return 0
            if root.val >= maxVal:
                return 1 + goodNodesHelper(root.left, root.val) + goodNodesHelper(root.right, root.val)
            return goodNodesHelper(root.left, maxVal) + goodNodesHelper(root.right, maxVal)
        return goodNodesHelper(root, float("-inf"))
        