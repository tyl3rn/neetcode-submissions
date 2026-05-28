# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root): 
            if not root:
                return
            
            queue = deque([root])
            while queue:
                size = len(queue)
                curNodes = []
                for i in range(size):
                    curNode = queue.popleft()
                    curNodes.append(curNode.val)

                    if curNode.left:
                        queue.append(curNode.left)
                    if curNode.right:
                        queue.append(curNode.right)
                res.append(curNodes)
        res = []
        bfs(root)
        return res


            



        