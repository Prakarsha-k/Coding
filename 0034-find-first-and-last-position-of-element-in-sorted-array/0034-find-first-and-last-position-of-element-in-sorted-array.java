class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first=indices(nums,target,true);
        int last=indices(nums,target,false);
        return new int[]{first,last};
    }
    public static int indices(int[] nums,int target,boolean isFirst){
        int low=0;
        int index=-1;
        int high=nums.length-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if (nums[mid]==target){
                index=mid;
                if (isFirst)
                {
                    high=mid-1;
                }
                    else
                {
                    low=mid+1;
                }
             }
            else if(nums[mid]<target)
            {
                low=mid+1;
            }
            else{
                    high=mid-1;
                }
            }
        return index;
    }
}