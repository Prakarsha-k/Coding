class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def encode(word):
            mapping = {}
            res = []
            next_num = 0
            for c in word:
                if c not in mapping:
                    mapping[c] = next_num
                    next_num += 1
                res.append(mapping[c])
            return res
        
        pattern_code = encode(pattern)
        return [word for word in words if encode(word) == pattern_code]
