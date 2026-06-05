from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)
            
            if root1 == root2:
                return False
            
            if rank[root1] > rank[root2]:
                par[root2] = root1
                rank[root1] += rank[root2]
            else:
                par[root1] = root2
                rank[root2] += rank[root1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        
        return True
