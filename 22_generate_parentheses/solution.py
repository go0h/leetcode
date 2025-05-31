class Solution:

    def generateParenthesis(self, n: int) -> list[str]:

        result = []
        
        def gen_parent(s: str, n: int, open: int):
            
            if n == 0 and open == 0:
                return result.append(s)
            elif n == 0 and open == 1:
                return result.append(s + ')')
            
            if n > 0:
                gen_parent(s + '(', n - 1, open + 1)

            if open > 0:
                gen_parent(s + ')', n, open - 1)


        gen_parent('', n, 0)

        return result


if __name__ == '__main__':

    n = 3
    result = Solution().generateParenthesis(n)

    print(result)