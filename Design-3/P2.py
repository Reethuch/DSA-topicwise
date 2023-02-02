# TC : O(1) as searching in dict takes O(1)
# SC : O(capacity)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent = []
        self.cache = {}

    def get(self, key: int) -> int:
        # print("get0", self.recent, self.cache)
        if key in self.cache:
            self.recent.remove(key)
            self.recent.append(key)
            # print("get", self.recent, self.cache)
            return self.cache[key]
        # print("get2", self.recent)
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.recent.remove(key)
        elif len(self.cache.keys()) >= self.capacity:
            k = self.recent.pop(0)
            del self.cache[k]
        self.recent.append(key)
        self.cache[key] = value
        # print(key, value, self.cache, self.recent)