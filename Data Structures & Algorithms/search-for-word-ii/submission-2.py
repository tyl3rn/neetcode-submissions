class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        curr = tree
        for word in words:
            tree.insert(word)
        rows, cols = len(board), len(board[0])
        res = []
        def dfs(row, col, curr):
            if row<0 or row>=rows or col<0 or col>=cols:
                return
            char = board[row][col]
            if char == "#":
                return
            board[row][col] = "#"
            if char in curr.children:
                curr = curr.children[char]
                if curr.endOfWord:
                    res.append(curr.endOfWord)
                    curr.endOfWord = ""
                dfs(row-1, col, curr)
                dfs(row+1, col, curr)
                dfs(row, col-1, curr)
                dfs(row, col+1, curr)
            board[row][col] = char
            return
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, curr)
        return res



class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = ""

    def insert(self, word: str) -> None:    
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTree()
            node = node.children[char]
        node.endOfWord = word

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True 
        
        