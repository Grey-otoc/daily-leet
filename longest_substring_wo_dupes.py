def lengthOfLongestSubstring(s: str) -> int:
    hash_map = {}
    l = 0
    longest = 0

    for r, char in enumerate(s):
        if char in hash_map:
            l = max(l, hash_map[char] + 1)

        hash_map[char] = r
        longest = max(longest, r - l + 1)

    return longest
    
if __name__ == "__main__":
    print(lengthOfLongestSubstring("dvdf"))
