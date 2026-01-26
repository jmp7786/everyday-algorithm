from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lets make a buket sorting 
        # 1. scatter this 
        # 2. sort each buckets
        # 3. gather all buckets
        
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) -1, 0, -1):
            sub_list = buckets[i]
            for num in sub_list:
                result.append(num)
                if len(result) == k:
                    return result
                    