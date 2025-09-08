class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), 1, k, n);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, List<Integer> temp, int start, int k, int n) {
        if (temp.size() == k && n == 0) {
            result.add(new ArrayList<>(temp));
            return;
        }
        for (int i = start; i <= 9; i++) {
            if (n - i < 0) break;
            temp.add(i);
            backtrack(result, temp, i + 1, k, n - i);
            temp.remove(temp.size() - 1);
        }
    }
}
