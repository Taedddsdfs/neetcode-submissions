class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: #sorted
                res = min(res, nums[l])
                break 

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 #최솟값은 오른쪽에 
            else:
                r = m - 1 #최솟값은 왼쪽에
        return res