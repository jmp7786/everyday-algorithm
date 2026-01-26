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
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            bucket[freq].append(num)
        
        result = []
        limit = 0
        for i in range(len(bucket) -1, 0, -1):
            sub_list = bucket[i]
            for num in sub_list:
                result.append(num)
                limit += 1
                if limit == k:
                    return result
                    