


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = 0, 0, 0
        res = []

        while k < n + m:
            if i < m and j < n and nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            elif i < m and j < n and nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            elif i < m:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
            k += 1

        for i in range(n + m):
            nums1[i] = res[i]

if __name__ == '__main__':

    nums1 = [5,6,7,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    Solution().merge(nums1, n, nums2, n)

    print(' '.join([str(i) for i in nums1]))