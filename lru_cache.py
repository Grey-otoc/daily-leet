class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            oldest_key = next(iter(self.cache))
            self.cache.pop(oldest_key)
            self.cache[key] = value
        else:
            self.cache.pop(key, None)
            self.cache[key] = value

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    print(lRUCache.get(2))
    lRUCache.put(2, 6)
    print(lRUCache.get(1))
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    print(lRUCache.get(1))
    print(lRUCache.get(2))
