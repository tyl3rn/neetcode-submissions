class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]

            return node.endOfWord
        return dfs(0,self)
                    

            
