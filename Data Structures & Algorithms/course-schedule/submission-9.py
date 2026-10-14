class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        done = set()
        visiting = set()
        def dfs(course):
            if adjList[course] == []:
                done.add(course)
                return True
            if course in done:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            done.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            



