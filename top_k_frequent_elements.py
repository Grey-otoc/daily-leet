def topKFrequent(nums: list[int], k: int) -> list[int]:
    counts = {}

    for num in nums:
        counts[num] = 1 + counts.get(num, 0)
    
    frequencies = [[] for _ in range(len(nums) + 1)]

    for num, count in counts.items():
        frequencies[count].append(num)
    
    result = []
    for freq in frequencies[::-1]:
        for num in freq:
            result.append(num)
            if len(result) == k:
                return result

if __name__ == "__main__":
    print(topKFrequent([1,2,2,3,3,3], 2))
