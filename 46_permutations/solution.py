class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def gen_permutations(nums, pos):
            
            if pos == len(nums):
                result.append(nums[:])

            for i in range(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                gen_permutations(nums, pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        gen_permutations(nums, 0)

        return result

if __name__ == '__main__':

    nums = [1,2,3] 
    result = Solution().permute(nums)
    print(result)