class Node(): 
    val: int 
    key: int 
    next  = None
    prev = None
    

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = Node()        
        self.end = Node()        
        self.head.next = self.end
        self.head.prev = self.end
        self.end.next = self.head
        self.end.prev = self.head
        self.map = {}
        self.size = 0

    def get(self, key: int) -> int:
        # print(list(self.map.items()))
        node = self.map.get(key)
        if node:      
            self._remove(node.key)
            self._add(node.key, node.val)
            return node.val
        else: 
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(key)
        if self.capacity == self.size:     
            self._remove(self._get_last_key())
        
        self._add(key, value)


        
    def _get_last_key(self, ): 
        return self.end.prev.key

    def _remove(self, key): 
        node = self.map.get(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.map[key]
        self.size -=1

    def _add(self, key, val): 
        node = Node(key, val)
        self.map[key] = node

        tmp = self.head.next 
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node 
        self.size +=1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)