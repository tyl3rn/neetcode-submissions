class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjList = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
        visiting = set([beginWord])
        queue = deque([beginWord]) 
        res = 1
        while queue:
            n = len(queue)
            for i in range(n):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjList[pattern]:
                        if nei not in visiting:
                            visiting.add(nei)
                            queue.append(nei)
            res += 1
        return 0
            
        