class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node, target):
            visited = set()

            def search(course):
                if course == target:
                    return True

                visited.add(course)

                for next_course in graph[course]:
                    if next_course not in visited:
                        if search(next_course):
                            return True

                return False

            return search(node)

        return [dfs(a, b) for a, b in queries]