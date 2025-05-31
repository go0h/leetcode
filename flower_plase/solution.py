class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        count = 0
        i = 0
        field_size = len(flowerbed)
        while i < field_size:
            if ((i - 1 >= 0 and flowerbed[i - 1] == 0) or (i - 1 == -1)) \
                and flowerbed[i] == 0 \
                and ((i + 1 < field_size and flowerbed[i + 1] == 0) or (i + 1 == field_size)):
                count += 1
                i += 2
            else:
                i += 1

        return count >= n


if __name__ == '__main__':

    print(str(Solution().canPlaceFlowers([0,0,1,0,0], 1)))
