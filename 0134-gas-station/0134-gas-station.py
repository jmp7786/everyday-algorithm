class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        amount = 0 
        start = 0
        for i in range(len(gas)): 
            print(i, amount, start)
            amount += gas[i]
            amount -= cost[i]
            if amount < 0: 
                start = i +1
                amount = 0
        return start