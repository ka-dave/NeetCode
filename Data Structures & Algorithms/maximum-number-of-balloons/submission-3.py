class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter('balloon')

        res = float('inf')
        for i in balloon:
            res = min(res, countText[i] // balloon[i])
        return res