import math

class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        
        if 8 <= N <= 11:
            return 11
        
        for length in range(1, 6):
            for half in range(10**(length-1), 10**length):
                s = str(half)
                pal = int(s + s[-2::-1])
                if pal >= N and is_prime(pal):
                    return pal
