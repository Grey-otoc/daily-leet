def findDuplicate(nums: list[int]) -> int:
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            return abs(num)
        else:
            nums[idx] *= -1
            
if __name__ == "__main__":
    print(findDuplicate([1,2,3,6,4,2,5]))
