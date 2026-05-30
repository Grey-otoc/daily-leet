def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    ROWS = len(matrix)
    COLS = len(matrix[0])
    l, r = 0, ROWS * COLS
    
    while l < r:
        midpoint = l + ((r - l) // 2)
        row = midpoint // COLS
        col = midpoint % COLS
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            r = midpoint
        elif matrix[row][col] < target:
            l = midpoint + 1

    return False

if __name__ == "__main__":
    print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 9))
