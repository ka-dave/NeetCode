class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []

        for i in range(len(temperatures)):
            found = False
            stack.clear()
            stack.append(temperatures[i])
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(len(stack))
                    found = True
                    break
                else:
                    stack.append(temperatures[j])     
            if not found:
                result.append(0) 
        return result