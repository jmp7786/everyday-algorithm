class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        graph = defaultdict(list)

        for to, src in prerequisites: 
            graph[src].append(to)
            indegree[src] = indegree.get(src, 0)
            indegree[to] = indegree.get(to, 0) +1

        zero_q = []
        result = []        
        for i in range(numCourses): 
            if i in indegree and indegree[i] == 0: 
                zero_q.append(i)        
            if i not in indegree:
                result.append(i)        

        while zero_q: 
            n = zero_q.pop()
            result.append(n)
            if n in graph:
                for i in graph[n]:
                    indegree[i] -= 1
                    if indegree[i] <= 0:
                        zero_q.append(i)
        
        return len(result) == numCourses
