def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
        midpoint = l + ((r - l) // 2)

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            r = midpoint
        elif nums[midpoint] < target:
            l = midpoint + 1

    return -1

if __name__ == "__main__":
    print(search([3,7,35,90,1012,12412414,888888888888,12931301239123801283], 888888888888))
