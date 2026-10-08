class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in prerequisites:
            adjList[u].append(v)
        visiting = set()
        done = set()

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
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                