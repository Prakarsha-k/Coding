class Solution:
    def decodeAtIndex(self, s: str, K: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        
        for c in reversed(s):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size //= int(c)
            else:
                size -= 1
