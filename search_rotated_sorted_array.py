def search(nums: list[int], target: int) -> int:
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] > target:
            l += 1
        elif nums[r] < target:
            r -= 1
        else:
            break
    
    while l <= r:
        midpoint = ((r - l) // 2) + l

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            l = midpoint + 1
        else:
            r = midpoint - 1

    return -1

if __name__ == "__main__":
    print(search([5,6,7,0,2,4], 0))
