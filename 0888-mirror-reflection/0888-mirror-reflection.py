import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = (p * q) // math.gcd(p, q)
        m = lcm // q
        n = lcm // p
        if m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 0
        elif m % 2 == 0 and n % 2 == 1:
            return 2
        return -1
