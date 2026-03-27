def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash_map = {}

    for num in nums:
        hash_map[num] = 1 + hash_map.get(num, 0)
    
    map_sorted = sorted(hash_map.items(), key=lambda pair: pair[1], reverse=True)
    
    return [pair[0] for pair in map_sorted[:k]]
