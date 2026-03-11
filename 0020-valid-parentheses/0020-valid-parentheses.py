class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'[': ']', '(': ')', '{': '}'}
        stack = []
        for st in s:
            if st in brackets.keys():
                stack.append(brackets[st])
            else:
                if not stack:
                    return False
                b = stack.pop()
                if st != b:
                    return False
        
        if stack: return False
        else: return True
            

            