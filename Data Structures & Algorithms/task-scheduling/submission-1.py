from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = max(count.values())
        maxCount = sum(1 for freq in count.values() if freq == maxFreq)

        answer = (maxFreq - 1) * (n + 1) + maxCount

        return max(len(tasks), answer)

        # (maxFreq - 1) * (n + 1) + maxCount 공식임 
        #A B _ | A B _ | A B 