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

        for i in stack:
            if re.search(r"[a-z1-9]\d*/", i):
                count += 1

        return count