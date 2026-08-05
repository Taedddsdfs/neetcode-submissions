class Solution:
    def removeLeafNodes(self, root, target):
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        return dfs(root)