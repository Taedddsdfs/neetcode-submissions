class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find data structure functions
        def find(parent, i):
            if parent[i] == -1:
                return i
            else:
                root = find(parent, parent[i])
                parent[i] = root  # path compression
                return root
        
        def union(parent, i, j):
            root_i = find(parent, i)
            root_j = find(parent, j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        # Initialize Union-Find data structure
        parent = [-1] * n  # each node is its own parent initially
        
        # Process each edge and perform union
        for edge in edges:
            a, b = edge
            union(parent, a, b)
        
        # Count the number of unique root parents (connected components)
        unique_components = len([i for i, p in enumerate(parent) if p == -1])
        
        return unique_components
