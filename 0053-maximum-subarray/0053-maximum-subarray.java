import java.util.*;
class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum=Integer.MIN_VALUE;
        int add=0;
        for (int i=0;i<nums.length;i++){
            add+=nums[i];
            if (add>max_sum){
                max_sum=add;
            }
            if (add<0){
                add=0;
            }
        }
        return max_sum;
    }
}