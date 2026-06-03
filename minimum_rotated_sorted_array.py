def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        midpoint = ((r - l) // 2) + l

        if nums[midpoint] > nums[r]:
            l = midpoint + 1
        else:
            r = midpoint 

    return nums[l]

if __name__ == "__main__":
    print(findMin([3,4,5,6,1,2]))
