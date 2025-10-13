class Solution:
    def trimMean(self, arr):
        arr.sort()
        n = len(arr)
        k = n // 20
        arr = arr[k:n - k]
        return sum(arr) / len(arr)
