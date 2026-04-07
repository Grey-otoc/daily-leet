def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) == 3 and sum(nums) != 0:
        return []
    
    sols = []
    nums.sort()

    for i, num in enumerate(nums):
        # in sorted array, if first num is > 0, solution is not possible
        if num > 0:
            break

        if i > 0 and num == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = num + nums[l] + nums[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                sols.append([num, nums[l], nums[r]])
                l += 1
                r -= 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return sols

if __name__ == "__main__":
    print(threeSum([0,0,0,0]))
