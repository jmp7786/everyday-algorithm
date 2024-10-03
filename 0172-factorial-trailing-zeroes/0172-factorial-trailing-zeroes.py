class Solution:
    def trailingZeroes(self, n: int) -> int:
        n = math.factorial(n)
        count = 0
        while n % 10 == 0:
            # print(count)
            n  = n // 10
            # print(n)
            count +=1

        
        return count