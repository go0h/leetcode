class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = 0
        left = 0
        right = len(nums)
        pos = (left + right) // 2
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
                if target > nums[mid]:
                    pos = mid + 1
            else:
                right = mid
                if target < nums[mid]:
                    pos = mid
        return pos

if __name__ == '__main__':

    nums = [5,6,7,7,8,10]
    target = 6

    result = Solution().searchInsert(nums, target)
    print(result)
