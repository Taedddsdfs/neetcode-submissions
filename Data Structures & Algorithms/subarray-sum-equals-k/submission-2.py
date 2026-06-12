class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cursum = 0
        prefixSums = {0:1} # prefix sum 이 0인 상태가 1번 존재한다
        for num in nums:
            cursum+=num
            diff = cursum-k # P[i] - P[j] = k difference 있으면 횟수 더하기 ㄱㄱ
            res+=prefixSums.get(diff,0)
            prefixSums[cursum] = 1+prefixSums.get(cursum,0)

        return res