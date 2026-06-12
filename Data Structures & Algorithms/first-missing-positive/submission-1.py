class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(nums)
        
        for i in range(1, n + 2):
            if i not in num_set:
                return i