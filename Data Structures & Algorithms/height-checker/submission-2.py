class Solution:
    def heightChecker(self, heights: List[int]) -> int:
         
        sorted_h = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if sorted_h[i] != heights[i]:
                res += 1
        return res