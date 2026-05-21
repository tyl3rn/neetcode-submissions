class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        # 4#poop3#cat
        res = []
        while s:
            i = 0
            while s[i] != '#':
                i+=1
            num = int(s[:i])
            string = s[i+1:i+1+num]
            res.append(string)
            s = s[i+1+num:]
        return res
                
