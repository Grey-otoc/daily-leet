def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
