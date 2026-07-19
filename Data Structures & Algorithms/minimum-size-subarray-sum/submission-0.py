class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = l = 0
        ans = float("inf")

        for r in range(len(nums)):
            res += nums[r]
            while res>=target:
                ans = min(ans,r-l+1)
                res-=nums[l]
                l+=1
            
        return 0 if ans == float("inf") else ans