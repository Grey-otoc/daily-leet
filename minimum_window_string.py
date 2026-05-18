def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    count_t = {char: t.count(char) for char in t}
    window = {}

    # represents the number of unique characters we need to have
    # in our window (not including the count of each)
    need = len(count_t)
    # how many required unique chars we currently have in window
    have = 0
    l = 0
    res = [-1, -1]
    res_len = 1001

    for r, char in enumerate(s):
        # increment count of curr char in window
        window[char] = 1 + window.get(char, 0)
        # if we now have required count of a char from t, then increment have
        if char in count_t and window[char] == count_t[char]:
            have += 1
        
        # once we have correct chars and correct count, look for a new window
        # continue moving l ptr forward until window no longer has all the chars required
        # ^ this signifies the start of a new potential window, which could be shorter
        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1

            # decrement count of char at l ptr in window
            window[s[l]] -= 1
            # if count of char at l ptr has just dropped below 
            # required amount, then decrement from have
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            
            l += 1

    l, r = res
    return s[l:r+1] if res_len != 1001 else ""

if __name__ == "__main__":
    print(minWindow("ASDWAWZA", "SWZ"))
