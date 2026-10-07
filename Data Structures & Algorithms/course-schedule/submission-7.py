class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adjList = defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False #loop, invalid
            if adjList[crs] == []:
                return True
            visited.add(crs)
            for course in adjList[crs]:
                if not dfs(course):
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        
            