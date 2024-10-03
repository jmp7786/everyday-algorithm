class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        visited = set((0,0))
        while min_heap and k > 0:
            val, i, j = heapq.heappop(min_heap)
            ans.append((nums1[i],nums2[j]))
            if i+1 < n and (i+1,j) not in visited: 
                heapq.heappush(min_heap, (nums1[i+1]+ nums2[j], i+1, j))
                visited.add((i+1,j))
            if j+1 < m and (i, j+1) not in visited: 
                heapq.heappush(min_heap, (nums1[i]+ nums2[j+1], i, j+1))
                visited.add((i, j+1))
            
            k -= 1
        
        return ans

        