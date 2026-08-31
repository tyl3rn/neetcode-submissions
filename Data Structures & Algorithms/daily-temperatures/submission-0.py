class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures) -1, -1, -1):
            while stack:
                curr = stack[-1]
                if temperatures[i] < temperatures[curr]:
                    res[i] = curr - i
                    break
                else:
                    stack.pop()

            stack.append(i)
                
        return res


