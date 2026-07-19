class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for ind, ele in enumerate(temperatures):
            while stack and stack[-1][0] < ele:
                stk_e, stk_i = stack.pop()
                result[stk_i] = ind - stk_i
            
            stack.append((ele, ind))
        
        return result