import collections

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    # deque = double sided queue
    # in our case it will be a monotonically (always) decreasing stack
    queue = collections.deque()
    l = 0
    r = 0 

    while r < len(nums):
        # if q not empty and curr num is > last num in deque, then
        # we can replace last num with curr num (and continue doing so)
        # until no other nums in deque or other num(s) > curr num
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)

        # since we are looking at a sliding window, we must remove any
        # out of bound indexes in deque, if l > first index in deque, first index
        # in deque must be outside of window
        if l > queue[0]:
            # pops first num from deque
            queue.popleft()
        
        # if window size == to k, then left ptr must move forward and max value
        # can be appended to res
        if r - l + 1 == k:
            res.append(nums[queue[0]])
            l += 1

        r += 1

    return res

if __name__ == "__main__":
    print(maxSlidingWindow([1,2,1,0,4,2,6], 3))
