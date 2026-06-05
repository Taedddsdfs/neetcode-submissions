class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visit = set()
        valid ={i:[] for i in range(n)}
        for n1,n2 in edges:
            valid[n1].append(n2)
            valid[n2].append(n1) #undirected so...
        
        def dfs(edge,prev): #checking cycle
            if edge in visit:
                return False
            visit.add(edge)
            for i in valid[edge]:
                if i == prev:
                    continue
                if not dfs(i,edge):
                    return False

            return True
        
        return dfs(0,-1) and n ==len(visit)