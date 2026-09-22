class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        # graph[u] = u를 들은 뒤 들을 수 있는 과목
        graph = [[] for _ in range(numCourses)]

        for pre, crs in prerequisites:
            graph[pre].append(crs)

        def dfs(start, target):
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

            return search(start)

        return [dfs(pre, crs) for pre, crs in queries]