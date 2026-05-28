# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        # do in order traversal 

        def inOrder(root: Optional[TreeNode]) -> None:
            if not root:
                return 
            inOrder(root.left)
            stack.append(root)
            inOrder(root.right)
        inOrder(root)
        return stack[k-1].val