class Solution:

    def jump(self, nums: list[int]) -> int:

        near = 0
        far = 0
        jumps = 0
        while far < len(nums) - 1:
            farthest = 0

            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])

            near = far + 1
            far = farthest
            jumps += 1

        return jumps

if __name__ == '__main__':

    # nums = [2,3,1,1,4]
    nums = [2,3,0,1,4]
    # nums = [0]
    # nums = [0, 2]
    # nums = [3,2,1]
    # nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    result = Solution().jump(nums)
    print(result)