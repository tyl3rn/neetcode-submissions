class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        for v, u in prerequisites: 
            adjList[u].append(v)
            indegree[v] += 1
        
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in adjList[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == numCourses else []
            