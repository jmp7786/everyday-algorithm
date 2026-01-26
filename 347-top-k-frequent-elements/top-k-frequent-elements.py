import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. counting frequency for all num 
        # 2. create a heap for
        # 3. iterate map for insert to min heap 
        # 4. pop k time for return values 
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        min_heap = []
        for key, value in counter.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
         
        return [key for value, key in min_heap]
            


        

         

        