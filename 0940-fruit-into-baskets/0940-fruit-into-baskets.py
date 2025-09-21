class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = {}
        left = 0
        res = 0
        for right, fruit in enumerate(fruits):
            count[fruit] = count.get(fruit, 0) + 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
        return res
