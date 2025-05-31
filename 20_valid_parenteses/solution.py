class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for par in s:
            
            if par in ['{', '[', '(']:
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                
                if par == '}' and stack[-1] == '{' or \
                    par == ']' and stack[-1] == '[' or \
                    par == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False

        return len(stack) == 0

if __name__ == '__main__':

    s = "()))"
    s = "()[]{}"
    s = "([])"
    result = Solution().isValid(s)

    print(result)