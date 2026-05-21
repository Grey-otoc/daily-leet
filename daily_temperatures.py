def dailyTemperatures(temperatures: list[int]) -> list[int]: 
    result = []
    stack = []

    for r in range(len(temperatures)-1, -1, -1):
        while stack and temperatures[r] >= temperatures[stack[-1]]:
            stack.pop()
        
        if stack:
            result.append(stack[-1] - r)
        else:
            result.append(0)
        
        stack.append(r)
    
    return result[::-1]
    
if __name__ == "__main__":
    print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
