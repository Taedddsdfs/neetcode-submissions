class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        graph = [[] for _ in range(numCourses)]

        # [a, b] = a가 b의 prerequisite
        for a, b in prerequisites:
            graph[a].append(b)

        def hasPath(start, target):
            visited = set()

            def dfs(course):
                if course == target:
                    return True

                visited.add(course)

                for next_course in graph[course]:
                    if next_course not in visited:
                        if dfs(next_course):
                            return True

                return False

            return dfs(start)

        return [hasPath(a, b) for a, b in queries]