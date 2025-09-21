class Solution {
    public int bestRotation(int[] nums) {
        int n = nums.length;
        int[] change = new int[n];
        for (int i = 0; i < n; i++) {
            int low = (i - nums[i] + 1 + n) % n;
            int high = (i + 1) % n;
            change[low]--;
            change[high]++;
            if (low > high) change[0]--;
        }
        int maxScore = -n, score = 0, bestK = 0;
        for (int k = 0; k < n; k++) {
            score += change[k];
            if (score > maxScore) {
                maxScore = score;
                bestK = k;
            }
        }
        return bestK;
    }
}
