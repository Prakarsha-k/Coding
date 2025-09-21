class Solution:
    def atMostNGivenDigitSet(self, D: list[str], N: int) -> int:
        S = str(N)
        K = len(S)
        n = len(D)
        res = sum(n**i for i in range(1, K))
        
        for i in range(K):
            has_same_num = False
            for d in D:
                if d < S[i]:
                    res += n**(K-i-1)
                elif d == S[i]:
                    has_same_num = True
            if not has_same_num:
                return res
        return res + 1
