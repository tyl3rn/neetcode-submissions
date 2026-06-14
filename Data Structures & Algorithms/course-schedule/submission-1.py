class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in prerequisites:
            adjList[u].append(v)
        def dfs(node, path):
                if node in path:
                    return False
                path.add(node)
                for value in adjList[node]:
                    if not dfs(value,path):
                        return False
                path.remove(node)
                return True
                

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True

            
        
        
        
