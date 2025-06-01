class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []

        def combine(candidates, pos, remainder, backtrack):

            if pos >= len(candidates) or remainder < 0:
                return

            if remainder == 0:
                combinations.append(backtrack)

            for i in range(pos, len(candidates)):
                if candidates[i] <= remainder:
                    combine(candidates, i, remainder - candidates[i], backtrack + [candidates[i]])

        combine(sorted(candidates), 0, target, [])

        return combinations

if __name__ == '__main__':

    candidates = [3,12,9,11,6,7,8,5,4]
    target = 15

    result = Solution().combinationSum(candidates, target)
    print(result)
