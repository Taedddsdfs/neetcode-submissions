class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for c in nums:
            if c in seen:
                return True
            seen.add(c)
        return False
