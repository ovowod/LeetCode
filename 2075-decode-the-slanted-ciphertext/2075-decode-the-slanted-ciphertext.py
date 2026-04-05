class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        
        n = len(encodedText)
        cols = n // rows
        encoded = []
        res = ''
        
        for i in range(rows):
            row = encodedText[i * cols + i : (i + 1) * cols]
            row += ' ' * i
            encoded.append(row)

        for i in range(len(encoded[-1])):
            for en in encoded:
                res += en[i]
        
        return res.rstrip()


        
        