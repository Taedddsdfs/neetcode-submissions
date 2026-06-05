class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n==1:
            return 1
        count = 0
        edmap = {i:[]for i in range(n)}
        visit = set()
        for n1,n2 in edges:
            edmap[n1].append(n2)
            edmap[n2].append(n1)
        def dfs(node):
            for n1 in edmap[node]:
                if n1 not in visit:
                    visit.add(n1)
                    dfs(n1)
        for n1 in edmap:
            if n1 in visit:
                continue
            visit.add(n1)
            count+=1
            dfs(n1)
        return count