class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int t_sum = n * (n + 1) / 2;
        int ele_sum = 0;

        for (int num : nums) {
            ele_sum += num;
        }

        return t_sum - ele_sum;
    }
};
    