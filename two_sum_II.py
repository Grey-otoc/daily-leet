def twoSum(numbers: list[int], target: int) -> list[int]:
    hash_map = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement] + 1, i + 1]
        
        hash_map[num] = i
        
if __name__ == "__main__":
    print(twoSum([1, 2, 3, 4], 3))
