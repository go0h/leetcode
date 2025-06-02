class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        
        length = 10

        seen = dict()
        result = []

        for i in range(len(s) - length + 1):
            current_str = s[i : length + i]
            seen[current_str] = seen.get(current_str, 0) + 1

        for k, v in seen.items():
            if v > 1:
                result.append(k)

        return result


if __name__ == '__main__':

    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    result = Solution().findRepeatedDnaSequences(s)
    print(result)