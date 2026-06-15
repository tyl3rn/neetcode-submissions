class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Given: 
            - Number of nodes
            - All undirected edges
        Task:
            -Determine if these edges make up a valid tree
        
        Intuition:
            -Some trick to find out if edges are valid
        
        To be a valid tree:
        All nodes must be connected
        There must be no cycles


        0 -> [1, 3]
        1 -> [0, 3]
        2 -> [4]
        3 -> [1, 0]
        4 -> [2]

        '''
        visited = set()
        if n-1 != len(edges):
            return False
        mapp = defaultdict(list)
        for u, v in edges:
            mapp[u].append(v)
            mapp[v].append(u) 
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for child in mapp[node]:
                dfs(child)
        dfs(0)
        return len(visited) == n


