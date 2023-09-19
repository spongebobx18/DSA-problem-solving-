class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                p = stack.pop()
                t = stack.pop()
                if i == "+":
                    stack.append(int(t) + int(p))
                elif i== "-":
                    stack.append(int(t) - int(p))
                elif i == "*":
                    stack.append(int(t) * int(p))
                else:
                    stack.append(int(t) / int(p))
            
            else:
                stack.append(int(i))
        return int(stack[-1])