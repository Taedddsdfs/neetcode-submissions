class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        n = len(piles)
        res = r
        while l<=r:
            m = (l+r)//2
            totaltime =0
            for p in piles:
                totaltime+=math.ceil(p/m)
            if totaltime>h:
                l= m+1
            elif totaltime<=h:
                r = m-1
                res = min(res,m)
        return res