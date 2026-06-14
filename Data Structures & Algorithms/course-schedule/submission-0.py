class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Create a graph of nodes and if you can visit every ndoe then it is possible 
        #just jotting, [0,1] would be row 0 col 1, and [1,0] is row 1, col 0
        #and u cant visit every node, so its false
        ''' 
        create adjancency list for each direction
        we can't call dfs starting from a root node and check for duplicates using a set
        because two nodes can have paths to the same pre req (and thus be a false positive)


        '''
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

            
        
        
        
