class Solution {
    public int findNumbers(int[] nums) {
        int count=0;
        for (int i=0;i<nums.length;i++){
            char [] digits=Integer.toString(nums[i]).toCharArray();
            int n_digits=digits.length;
            if (n_digits%2==0){
                count+=1;
            }
        }
        return count;
    }
}