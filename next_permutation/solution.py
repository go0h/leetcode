class Solution:

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # go from end to start, and find first non descending number
        idx1 = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx1 = i
                break
    
        ## check if last permutation, descending order
        if idx1 == -1:
            nums.sort()
            return

        idx2 = -1
        # find the next greater element and swap it with idx2
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[idx1]:
                idx2 = i
                break

        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        s = idx1 + 1
        e = len(nums) - 1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
        
if __name__ == '__main__':
    nums = [1,3,2] # 14253
    Solution().nextPermutation(nums)
    print(nums)