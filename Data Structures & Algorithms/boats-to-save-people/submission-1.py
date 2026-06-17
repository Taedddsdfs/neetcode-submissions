class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0

        people.sort()
        l,r = 0, len(people)-1
        while l<=r: # 마지막 사람 고려
            remain = limit-people[r]
            r-=1
            boats+=1
            if l<=r and remain >= people[l]:
                l+=1
        return boats