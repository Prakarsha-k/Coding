class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1, n):
            prev = s
            s = ""
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:
                    s += str(count) + prev[i-1]
                    count = 1
            s += str(count) + prev[-1]
        return s
