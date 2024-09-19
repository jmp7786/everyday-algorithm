class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        result = []
        visited = set()
        self.find(startGene, 0, visited, result, bank, endGene)
        return min(result)if result else -1

    def find(self, curr, level, visited, result, bank, endGene): 
        # print(1, curr, endGene, curr == endGene)
        if curr == endGene: 
            result.append(level)
            return 

        for i in range(len(bank)):
            if bank[i] not in visited and self.diff(curr, bank[i]): 
                visited.add(bank[i])
                self.find(bank[i], level+1, visited, result, bank, endGene)   
                visited.remove(bank[i])
        

    def diff(self, str1, str2): 
        count = 0
        for i in range(len(str1)): 
            if str1[i] != str2[i]: 
                count += 1 
        # print(str1, str2, count == 1)
        return count == 1

        