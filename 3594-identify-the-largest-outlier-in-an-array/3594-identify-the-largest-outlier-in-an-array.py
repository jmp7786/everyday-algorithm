class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        res = -inf
        for a in nums:
            outlier = total - a - a
            if count[outlier] > (outlier == a):
                res = max(res, outlier)
        return res

