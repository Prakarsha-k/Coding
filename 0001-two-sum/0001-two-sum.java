import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap<Integer,Integer>output=new HashMap<>();
       for (int i=0;i<nums.length;i++){
        int diff=target-nums[i];
        if (output.containsKey(diff)){
            if (i<output.get(diff)){
                return new int[]{i,output.get(diff)};
                }
            else{
                return new int[]{output.get(diff),i};
            }
        }
        output.put(nums[i],i);
       }
    return new int[]{-1,-1};
    }
}