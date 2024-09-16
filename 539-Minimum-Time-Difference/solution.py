from typing import List


class Solution:
    
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hh, mm = map(int, time.split(':'))
            minutes.append(hh * 60 + mm)

        minutes.sort()

        min_diff = float('inf')

        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        circular_diff = 1440 + minutes[0] - minutes[-1]
        min_diff = min(min_diff, circular_diff)

        return min_diff