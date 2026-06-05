def search(nums: list[int], target: int) -> int:    
    l, r = 0, len(nums) - 1

    while l <= r:
        midpoint = (l + r) // 2
        
        if nums[midpoint] == target:
            return midpoint
        
        if nums[l] <= nums[midpoint]:
            if target > nums[midpoint] or target < nums[l]:
                l = midpoint + 1
            else:
                r = midpoint - 1
                
        else:
            if target < nums[midpoint] or target > nums[r]:
                r = midpoint - 1
            else:
                l = midpoint + 1

    return -1

if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2,3], 0))
