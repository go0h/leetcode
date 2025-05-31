class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        p1 = 0
        p2 = 1
        while p2 < len(nums):

            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
            else:
                p2 += 1

        return p1 + 1

if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]

    result = Solution().removeDuplicates(nums)

    print(result, nums[0 : result])