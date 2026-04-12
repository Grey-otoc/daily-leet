def maxArea(heights: list[int]) -> int:
    if len(heights) == 2:
        return min(heights)
    
    maxArea = 0

    l = 0
    r = len(heights) - 1

    while l < r:
        maxArea = max(
            maxArea, min(heights[l], heights[r]) * (r - l)
        )

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return maxArea

if __name__ == "__main__":
    print(maxArea([1,7,2,5,4,7,3,6]))
