def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    k = 1000000000

    if len(piles) == h:
        return r

    while l < r:
        midpoint = ((r - l) // 2) + l
        total = 0

        for p in piles:
            hours = -(-p // midpoint)
            total += hours
            if total > h:
                break
        
        if total > h:
            l = midpoint + 1
        if total <= h:
            r = midpoint
            k = min(k, midpoint)

    return k

if __name__ == "__main__":
    print(minEatingSpeed([1,4,3,2], 9))
