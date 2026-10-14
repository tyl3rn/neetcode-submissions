class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        res = []
        done = set()
        visiting = set()
        def dfs(course):
            if course in done:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            res.append(course)
            done.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            