class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        res = []

        while True:
            s = 0
            for i in range(len(n)):
                s += int(n[i]) ** 2

            if s == 1:
                return True
            if s in res:
                return False
            
            res.append(s)
            n = str(s)