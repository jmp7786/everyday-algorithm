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
        
        min_heap = [(value, key) for key, value in counter.items()]
        heapq.heapify(min_heap)

        top_k = heapq.nlargest(k, min_heap)
        result = [tupl[1] for tupl in top_k ]
        return result
            


        

         

        