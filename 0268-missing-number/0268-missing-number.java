class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        int total_sum=(n*(n+1))/2;
        int arr_sum=0;
        for(int i=0;i<nums.length;i++){
            arr_sum+=nums[i];
        }
        return total_sum-arr_sum;
    }
}