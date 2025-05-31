# [4,5,6,7,8,0,1,2]
# [4,5,6,7,8,9,0,1,2]

# [4,5,6,7,0,1,2]

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        size = len(nums)
        left = 0
        right = size - 1
        pivot = 0

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            if left == right:
                pivot = left
        left = 0
        right = size
        while left < right:
            mid = (((left + right) // 2) + pivot) % size
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = (left + right) // 2 + 1
            else:
                right = (left + right) // 2
        return -1

if __name__ == '__main__':

    nums = [3,1]
    target = 3

    result = Solution().search(nums, target)
    print(result)
