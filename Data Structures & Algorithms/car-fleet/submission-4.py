class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            diff = (target - position[i])/speed[i]
            cars.append((position[i], diff))

        fleet = 0
        prev_slow_time = 0

        for pos, time in sorted(cars, reverse=True):
            if time > prev_slow_time:
                fleet += 1
                prev_slow_time = time
        
        return fleet