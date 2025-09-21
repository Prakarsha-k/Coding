class Solution:
    def numSpecialEquivGroups(self, A: list[str]) -> int:
        seen = set()
        for word in A:
            even = sorted(word[::2])
            odd = sorted(word[1::2])
            seen.add((tuple(even), tuple(odd)))
        return len(seen)
