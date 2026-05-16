def characterReplacement(s: str, k: int) -> int:
    char_counts = {chr(i): 0 for i in range(65, 91)}
    max_f = 0
    res = 0
    l = 0

    for r, char in enumerate(s):
        char_counts[char] += 1
        max_f = max(max_f, char_counts[char])

        window_len = (r - l + 1)
        if window_len - max_f <= k:
            res = max(res, window_len)
        else:
            char_counts[s[l]] -= 1
            l += 1

    return res

if __name__ == "__main__":
    print(characterReplacement("AAABAADSAS", 1))
