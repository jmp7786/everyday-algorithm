class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n
        for i in range(1, n): 
            flag = False
            for j in range(i): 
                curr = 0
                if nums[i] > nums[j]: 
                    memo[i] = max(memo[i], memo[j])
                    flag = True
                    # print('i, j', i, j, memo[i])
            if flag:
                memo[i] +=1 
                
        print(memo)
        return max(memo) +1
