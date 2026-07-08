class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) >= 1:
            print(self.stack)
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        result = self.stack[0]
        for i in range(1,len(self.stack)):
            if self.stack[i] <= result:
                result = self.stack[i]
            
        return result
