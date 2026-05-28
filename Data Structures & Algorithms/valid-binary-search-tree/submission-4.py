# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, max_val, min_val):
            if not root:
                return True
            if root.val <=min_val or root.val >=max_val:
                return False
            return isValid(root.left, root.val, min_val) and isValid(root.right, max_val, root.val)
        return isValid(root, float("inf"),float("-inf"))
        