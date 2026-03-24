from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n

        for i in range(2, int(sqrt(n))+1):
            if primes[i]:
                for j in range(i * 2, n, i):
                    primes[j] = False
        
        return primes[2:].count(True)
        
        