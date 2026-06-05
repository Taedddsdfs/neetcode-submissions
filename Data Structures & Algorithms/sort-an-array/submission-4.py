class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            # Create a frequency map for the numbers
            count = defaultdict(int)
            minVal, maxVal = min(nums), max(nums)
            
            # Count occurrences of each value
            for val in nums:
                count[val] += 1

            # Reconstruct the original array in sorted order
            index = 0
            for val in range(minVal, maxVal + 1):
                while count[val] > 0:
                    nums[index] = val
                    index += 1
                    count[val] -= 1

        counting_sort()
        return nums