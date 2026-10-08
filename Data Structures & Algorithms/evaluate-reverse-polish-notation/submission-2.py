class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-/*":
                num2 = stack.pop()
                num1 = stack.pop()
                operator = tokens[i]
                if operator == "+":
                    stack.append(num1 + num2)
                elif operator == "-":
                    stack.append(num1 - num2)
                elif operator == "*":
                    stack.append(num1 * num2)
                elif operator == "/":
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
            