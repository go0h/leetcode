class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        ht = dict()
        operations = 0
        for num in nums:

            if ht.get(k - num, 0) > 0:
                ht[k - num] -= 1
                operations += 1
            else:
                ht[num] = ht.get(num, 0) + 1

        return operations

if __name__ == '__main__':

    # nums = [1,2,3,4]
    # k = 5

    nums = [3,1,3,4,3]
    k = 6

    # num = [3,1,5,1,1,1,1,1,2,2,3,2,2]
    # k = 1
    result = Solution().maxOperations(nums, k)
    print(result)