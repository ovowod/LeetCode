class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        roman_hash = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

        for k, v in roman_hash.items():
            n = num // k
            res += v * n
            num = num - n * k
        
        return res


        

        