class Solution:

    # bruteforce
    # def subarraySum(self, nums: list[int], k: int) -> int:

    #     sub_arrays = 0
    #     for i in range(len(nums)):
    #         sum = 0

    #         for j in range(i, len(nums)):
    #             sum += nums[j]

    #             if sum == k:
    #                 sub_arrays += 1

    #     return sub_arrays
    
    # with extra space

    def subarraySum(self, nums: list[int], k: int) -> int:

        sub_arrays = 0
        curr_sum = 0
        ht = {curr_sum: 1}

        for i in range(len(nums)):
            print(ht)
            curr_sum += nums[i]

            if curr_sum - k in ht:
                sub_arrays += ht[curr_sum - k]

            ht[curr_sum] = ht.get(curr_sum, 0) + 1

        return sub_arrays

if __name__ == '__main__':

    nums = [1,1,1]
    k = 2

    # nums = [1,2,3]
    # k = 3

    nums = [1]
    k = 0

    nums = [1,-1,0]
    k = 0

    print(nums)
    result = Solution().subarraySum(nums, k)
    print(result)