from collections import defaultdict, deque


class Solution:

    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        if not prerequisites: 
            return [i for i in range(numCourses)]

        indegree = {}
        graph = defaultdict(list)
        for to, src in prerequisites: 
            graph[src].append(to)
            indegree[src] = indegree.get(src, 0)
            indegree[to] = indegree.get(to, 0) + 1
        
        zero_q = [k for k, v in indegree.items() if v == 0]

        result = []
        for i in range(numCourses): 
            if i not in indegree: 
                result.append(i)

        visited = set()

        while zero_q: 
            n = zero_q.pop()
            if n in result: 
                return []
            result.append(n)

            if n in graph: 
                for to in graph[n]: 

                    indegree[to] -= 1

                    if indegree[to] <= 0: 
                        zero_q.append(to)
            
        
        return result if len(result) == numCourses else []