class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:

            if nums[p1] == val:
                
                while nums[p2] == val and p1 < p2:
                    p2 -= 1
                
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1

            p1 += 1

        return p2 + 1

if __name__ == '__main__':

    nums = [3,2,2,3]
    val = 3

    # nums = [0,1,2,2,3,0,4,2]
    # val = 2

    # nums = [1]
    # val = 1

    result = Solution().removeElement(nums, val)

    print(result, nums[0 : result])