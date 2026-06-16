class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in prevmap:
                return[prevmap[diff]+1,i+1]
            prevmap[n]=i

