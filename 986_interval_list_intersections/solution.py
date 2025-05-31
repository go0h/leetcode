class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        idx_f = 0
        idx_s = 0
        result = []

        def get_intersection(fl: list[int], sl: list[int]) -> list[int]:            
            if sl[0] <= fl[0] <= sl[1] or fl[0] <= sl[0] <= fl[1]:
                return [max(fl[0], sl[0]), min(fl[1], sl[1])]
            return []
        
        intersect = []

        while idx_f < len(firstList) and idx_s < len(secondList):
            
            f = firstList[idx_f]
            s = secondList[idx_s]

            intersect = get_intersection(f, s)
            print(intersect)
            if intersect != []:
                result.append(intersect)

            if f[1] >= s[1]:
                idx_s += 1
            elif s[1] >= f[1]:
                idx_f += 1

        return result


if __name__ == '__main__':

    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(firstList)
    print(secondList)
    result = Solution().intervalIntersection(firstList, secondList)
    print(result)
