class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        majority = defaultdict(int)
        for n in nums:
            majority[n]+=1
        res = []
        for n,c in majority.items():
            if majority[n]>length/3:
                res.append(n)
        return res