def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    curr_window = [num for num in nums[:k]]
    res = []

    res.append(max(curr_window))

    for r in range(k, len(nums)):
        curr_window.append(nums[r])
        curr_window = curr_window[1:]
        res.append(max(curr_window))
        
    return res

if __name__ == "__main__":
    print(maxSlidingWindow([1,2,1,0,4,2,6], 3))
