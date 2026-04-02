def longestConsecutive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    num_set = set(nums)
    sequence_leaders = {}

    for num in num_set:
        if (num - 1) not in num_set:
            sequence_leaders[num] = [num]
                
    for key in sequence_leaders:
        next_val = sequence_leaders[key][-1] + 1
        while next_val in num_set:
            sequence_leaders[key].append(next_val)
            next_val += 1
    
    return len(max(sequence_leaders.values(), key=lambda val: len(val)))

if __name__ == "__main__":
    print(longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))
