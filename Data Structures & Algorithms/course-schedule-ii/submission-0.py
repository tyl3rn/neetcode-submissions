class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        for u, v in prerequisites:
            adjList[u].append(v)
        visiting = set()
        done = set()
        res = []
        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True
            visiting.add(course)
            for prereq in adjList[course]:
                if dfs(prereq) is False:
                    return False 
            visiting.remove(course)
            done.add(course)
            res.append(course)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
                