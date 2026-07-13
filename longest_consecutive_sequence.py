def longestConsecutive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    
    res = 0
    num_set = set(nums)
    
    for num in num_set:
        if num - 1 not in num_set:
            curr_len = 1
            
            while num + curr_len in num_set:
                curr_len += 1
                
            res = max(res, curr_len)
            
    return curr_len
    

if __name__ == "__main__":
    print(longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))
