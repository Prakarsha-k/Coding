class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        import math
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)
        def count(x):
            return x//a + x//b + x//c - x//ab - x//bc - x//ac + x//abc
        left, right = 1, 2*10**9
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1
        return left
