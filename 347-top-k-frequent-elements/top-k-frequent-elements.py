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
        
        bucket = [None] * (len(nums) + 1)
        for num, freq in counter.items():
            if bucket[freq] is None:
                bucket[freq] = list()
            bucket[freq].append(num)
        
        result = []
        limit = 0
        for i in range(len(bucket) -1, -1, -1):
            sub_list = bucket[i]
            if sub_list is not None:
                for num in sub_list:
                    if limit < k:
                        result.append(num)
                        limit += 1
                    else:
                        break
            
            if limit == k:
                break
        
        return result
