class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 + num2
                stack.append(res)                
            elif tokens[i] == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 - num2
                stack.append(res)
            elif tokens[i] =="*":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 * num2
                stack.append(res)
            elif tokens[i] == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
            