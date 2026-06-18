class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res, entries = (-1, ""), self.timemap.get(key, [])
        l, r = 0, len(entries) - 1

        while l <= r:
            midpoint = (r + l) // 2
            pair = entries[midpoint]

            if pair[0] > timestamp:
                r = midpoint - 1
            elif pair[0] <= timestamp:
                l = midpoint + 1

                if res[0] < pair[0]:
                    res = (pair[0], pair[1])

        return res[1]
            
if __name__ == "__main__":
    ["set", ["check", "one", 5], "set", ["check", "two", 10], "get", ["check", 7], "get", ["nonexistent", 7]]
    
    timeMap = TimeMap()
    timeMap.set("check", "one", 5)
    timeMap.set("check", "two", 10)
    print(timeMap.get("check", 7))
    print(timeMap.get("nonexistent", 7))
