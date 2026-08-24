class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0]*1000

        for num,start,end in trips:
            change[start]+=num
            change[end]-=num
        
        passengers = 0
        for x in change:
            passengers+=x

            if passengers>capacity:
                return False
        return True
