class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        res = 0
        def dfs(node):
            nonlocal res
            if node in visited:
                return 
            visited.add(node)
            for child in adjList[node]:
                dfs(child)

        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i)
        return res