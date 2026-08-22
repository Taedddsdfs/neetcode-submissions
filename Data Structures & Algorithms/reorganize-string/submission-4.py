class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxheap = [ (-cnt,char) for char,cnt in freq.items()]
        heapq.heapify(maxheap)

        prev = 0
        res = ""
        while maxheap or prev:
            if prev and not maxheap: #차피 cnt = 마이너스니깐 0될때까지 prev 연속안됨 
                return ""
            cnt,char = heapq.heappop(maxheap)
            res+=char
            cnt+=1

            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            if cnt!=0:
                prev = (cnt,char)
        return res  