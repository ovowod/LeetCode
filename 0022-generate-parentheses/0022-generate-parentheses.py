class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def parentheses(s, open, close):
            if open == n and close == n:
                result.append(''.join(s.copy()))
                return
            
            if open < n:
                s.append('(')
                parentheses(s, open + 1, close)
                s.pop()
            if close < open:
                s.append(')')
                parentheses(s, open, close + 1)
                s.pop()
        
        parentheses([], 0, 0)
        return result