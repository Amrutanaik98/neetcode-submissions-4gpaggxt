class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] ## to store opening brackets
        closeToOpen={")":"(","]":"[","}":"{"}

        for c  in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: ## check stack is not empy and matched the corresponding opening 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

