class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize
        transitive_closure = [[False for _ in range(numCourses)]
                                for _ in range(numCourses)]

        # Build graph
        graph = [[course] for course in range(numCourses)] # create cycle
        for fi_course, se_course in prerequisites:
            graph[fi_course].append(se_course)

        def dfs(source, u):
            transitive_closure[source][u] = True
            
            for v in graph[u]:
                if not transitive_closure[source][v]:
                        dfs(source, v)
                    
            return

        for course in range(numCourses):
            dfs(course, course)

        ans = [] 
        for first_course, second_course in queries:
            ans.append(transitive_closure[first_course][second_course])
        
        return ans