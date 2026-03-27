def groupAnagrams(strs:list[str]) -> list[list[str]]:
    if len(strs) == 1:
        return [[strs[0]]]
    
    hash_map = {}

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        
        count = tuple(count)
        
        if hash_map.get(count, 0) != 0:
            hash_map[count].append(s)
        else:
            hash_map[count] = [s]
    
    return [l for l in hash_map.values()]
