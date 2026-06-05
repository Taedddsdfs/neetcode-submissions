class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)
            if root1 == root2:
                return False
            if rank[root2] > rank[root1]:
                par[root1] = root2
                rank[root2] += rank[root1]
            else:
                par[root2] = root1
                rank[root1] += rank[root2]
            return True
        
        if len(edges) != n - 1:
            return False
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        
        # Check if all nodes are in the same connected component
        root = find(0)
        return all(find(i) == root for i in range(1, n))
