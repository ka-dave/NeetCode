class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        for i in tokens:
            if i == "+":
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(int(e2 + e1))
            elif i == "*":
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(int(e2 * e1))
            elif i == "-":
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(int(e2 - e1))
            elif i == "/": 
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(int(e2 / e1))
            else:
                stack.append(int(i))
        
        return stack[0]