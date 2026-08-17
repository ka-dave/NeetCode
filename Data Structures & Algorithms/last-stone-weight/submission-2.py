class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)

            first = stones.pop(0)
            second = stones.pop(0)

            if first == second:
                continue
            elif first - second:
                stones.insert(0, first-second)
        
        if stones:
            return stones[0]
        return 0