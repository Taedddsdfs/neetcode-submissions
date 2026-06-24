from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # Case 1: The left half is normally sorted
            if nums[l] <= nums[m]:
                # Check if target lies within the sorted left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Case 2: The right half is normally sorted
            else:
                # Check if target lies within the sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        # Return -1 if the target is not found in the array
        return -1