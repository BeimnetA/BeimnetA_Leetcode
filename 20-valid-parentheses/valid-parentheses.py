class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketHash = {")" : "(", "]" : "[", "}" : "{"}

        for i in s:
            if i in bracketHash:
                if stack and stack[-1] == bracketHash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False