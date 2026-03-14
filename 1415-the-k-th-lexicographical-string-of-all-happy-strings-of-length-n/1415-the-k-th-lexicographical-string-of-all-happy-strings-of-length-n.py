class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_list = []
        
        def happy_str(s, pre_str):
            if len(happy_list) == k:
                return
            elif len(s) == n:
                happy_list.append(''.join(s.copy()))
                return
            
            letters = ['a', 'b', 'c']
            for letter in letters:
                if pre_str == letter:
                    continue
                s.append(letter)
                happy_str(s, letter)
                s.pop()
            
        happy_str([], '')
        
        print(happy_list)
        if len(happy_list) < k:
            return ''
        return happy_list[k - 1]