"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapp = {}
        #returns cloned version of node with all neighbors as clones
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in mapp:
                return mapp[node]
            copy = Node(node.val)
            mapp[node] = copy
            for neighbor in node.neighbors:
                if neighbor in mapp:
                    copy.neighbors.append(mapp[neighbor])
                else:
                    #returns cloned version of node with all neighbors handled 
                    copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)





            
        


        