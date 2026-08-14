class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap= []
        for n in nums:
            heapq.heappush(minheap,-n)
        heapq.heapify(minheap)
        
        for i in range(k):
            res = heapq.heappop(minheap)
        return -res
