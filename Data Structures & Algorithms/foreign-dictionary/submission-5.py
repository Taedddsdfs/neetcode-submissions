class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                
        visit = {} # False = default value for indicating it is not on the path
        # True = visited on the path
        res =[]
        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True # visited and on the path to detect the cycle.
            for neichar in adj[char]:
                if dfs(neichar):
                    return True
            visit[char] = False # not on the path anymore
            adj[char] =[]
            res.append(char)
        for char in adj:
            if dfs(char): # detected a loop
                return "" 
        res.reverse() # due to Post Order DFS
        return "".join(res)

