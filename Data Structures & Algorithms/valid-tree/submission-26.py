class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node,parent):

            if node in visited:
                return False
            
            visited.add(node)

            for nod in graph[node]:
                if nod == parent:
                    continue        # undirected -> parent 로 돌아갈수잇음
                if not dfs(nod,node):
                    return False
        
            return True

        return dfs(0,-1) and len(visited) == n 
