import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. counting frequency for all num 
        # 2. create a heap forl;kj
        # 3. iterate map for insert to min heap 
        # 4. pop k time for return values 
        counter = defaultdict(int)
        for i in range(len(nums)):
            counter[nums[i]] += 1
        
        heap = []
        limit = 0
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
         
        return result
            


        

         

        