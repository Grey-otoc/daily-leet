def get_kth(a: list[int], m: int, b: list[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n:
            return get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[b_start + k - 1]
        if k == 1:
            return min(a[a_start], b[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    left = (len(nums1) + len(nums2) + 1) // 2
    right = (len(nums1) + len(nums2) + 2) // 2
    return (get_kth(nums1, len(nums1), nums2, len(nums2), left) +
            get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0

if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [2, 4, 7]))
