import re

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        count = 0

        for i in logs:
            if i == '../':
                if stack:
                    stack.pop()
            elif i == './':
                continue
            else:
                stack.append(i)

        return len(stack)