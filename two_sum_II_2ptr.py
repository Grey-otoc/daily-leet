def twoSum(numbers: list[int], target: int) -> list[int]:
    lptr = 0
    rptr = len(numbers) - 1
    
    while lptr < rptr:
        sum = numbers[lptr] + numbers[rptr]
        
        if sum < target:
            lptr += 1
        elif sum > target:
            rptr -= 1
        else:
            return [lptr + 1, rptr + 1]
            
if __name__ == "__main__":
    print(twoSum([1, 2, 3, 4], 3))
