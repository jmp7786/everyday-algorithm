class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        # print('insert self.list', self.list, val)
        n = len(self.list)
        self.map[val] = n
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: 
            return False
        # print('remove self.list', self.list, val)
        # print('remove self.map', self.map)
        idx = self.map.get(val)
        tmp = self.list[idx]
        
        swaped = self.list[-1]
        self.list[idx] = swaped
        self.list[-1] = tmp
        self.list.pop()
        self.map[swaped] = idx
        del self.map[val]
        # print('remove2 self.list', self.list, val)
        return True


    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()