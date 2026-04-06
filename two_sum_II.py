def twoSum(numbers: list[int], target: int) -> list[int]:
    for i, num in enumerate(numbers):
        complement = target - num
        if complement == num:
            continue
        
        if complement in numbers[i + 1:]:
            complementInd = numbers[i + 1:].index(complement) + i + 1
            return [i + 1, complementInd + 1]
        
if __name__ == "__main__":
    print(twoSum([1, 2, 3, 4], 3))
