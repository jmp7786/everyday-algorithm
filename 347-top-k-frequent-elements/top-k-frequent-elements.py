from collections import Counter
import random 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        uniques = list(freq_map.keys())
        slice_idx = self._quick_select(uniques, freq_map, 0, len(uniques)-1, len(uniques)-k)
        return uniques[slice_idx:]

    def _quick_select(self, nums: List[int], freq_map: dict, left: int, right: int, k_smallest: int) -> int:
        if left >= right:
            return right
        
        pivot_idx = random.randint(left, right)
        new_pivot_idx = self._partition(nums, freq_map, left, right, pivot_idx)
        if new_pivot_idx == k_smallest:
            return new_pivot_idx
        elif new_pivot_idx > k_smallest:
            return self._quick_select(nums, freq_map, left, new_pivot_idx-1, k_smallest)
        else:
            return self._quick_select(nums, freq_map, new_pivot_idx+1, right, k_smallest)

        

    def _partition(self, nums: List[int], freq_map: dict, left: int, right: int, pivot_idx: int) -> int:
        freq = freq_map[nums[pivot_idx]]

        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        
        for i in range(left, right):
            if freq >= freq_map[nums[i]]:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx +=1
        
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        
        return store_idx

        
