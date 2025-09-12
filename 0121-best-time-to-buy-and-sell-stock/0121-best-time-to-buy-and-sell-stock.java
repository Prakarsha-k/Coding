class Solution {
    public int maxProfit(int[] prices) {
        int max_prof=0;
        int buy=prices[0];
        for (int i=1;i<prices.length;i++){
            if (prices[i]<buy){
                buy=prices[i];
            }
            else{
                int profit=prices[i]-buy;
                if (profit>max_prof){
                    max_prof=profit;
                }
            }
        }
        return max_prof;
    }
}
