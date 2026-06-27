class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(largest):
            subarr = 1 
            curSum =0
            for num in nums:
                curSum+=num

                if curSum > largest:
                    subarr+=1

                    if subarr>k:
                        return False
                    curSum = num

            return True
        
        l,r = max(nums),sum(nums)
        res = r
        while l<=r:
            mid = (l+r)//2
            if canSplit(mid):
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1
        return res


        