class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        if len(s)!=len(t):
            return False
        for c in s:
            count1[c]+=1
        for c in t:
            count2[c]+=1
        for c in s:
            if count1[c]!= count2[c]:
                return False
        return True