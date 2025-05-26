class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.usage=[]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.usage:
            self.usage.remove(key)
        elif len(self.cache)>=self.capacity:
            lru=self.usage.pop(0)
            del self.cache[lru]
        self.cache[key]=value
        self.usage.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)