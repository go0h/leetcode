class Solution:
    
    def letterCombinations(self, digits: str) -> list[str]:

        buttons = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        result = []

        def dfs(digits, num_i, s, res):

            if num_i == len(digits):
                return res.append(s) if s != "" else res

            button = int(digits[num_i])

            for char in buttons[button]:
                next_str = s + char
                dfs(digits, num_i + 1, next_str, res)

            return res
        
        dfs(digits, 0, "", result)

        return result



if __name__ == '__main__':

    digits = "23"
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    result = Solution().letterCombinations(digits)

    print(result)