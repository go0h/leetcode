class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def find_combinations(candidates, pos, previous, remainder, backtrack):

            if remainder < 0:
                return
            if remainder == 0 and backtrack not in result:
                result.append(backtrack)

            for i in range(pos, len(candidates)):
                if previous >= 0 and candidates[previous] == candidates[i]:
                    continue
                if candidates[i] <= remainder:
                    find_combinations(
                        candidates,
                        i + 1,
                        previous,
                        remainder - candidates[i],
                        backtrack + [candidates[i]]
                    )
                    previous = i

        find_combinations(sorted(candidates), 0, -1, target, [])

        return result

if __name__ == '__main__':

    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 15

    result = Solution().combinationSum2(candidates, target)
    print(result)

