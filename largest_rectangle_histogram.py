def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for r, h in enumerate(heights):
        start = r
        while stack and stack[-1][1] > h:
            l, l_height = stack.pop()
            max_area = max(max_area, (l_height * (r - l)))
            start = l
    
        stack.append((start, h))

    for l, h in stack:
        max_area = max(max_area, h * (len(heights) - l))
        
    return max_area

if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))
