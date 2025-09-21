import java.util.*;

class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] r : richer) graph[r[1]].add(r[0]);
        
        int[] res = new int[n];
        Arrays.fill(res, -1);
        for (int i = 0; i < n; i++) dfs(i, graph, quiet, res);
        return res;
    }
    
    private int dfs(int u, List<Integer>[] graph, int[] quiet, int[] res) {
        if (res[u] != -1) return res[u];
        res[u] = u;
        for (int v : graph[u]) {
            int cand = dfs(v, graph, quiet, res);
            if (quiet[cand] < quiet[res[u]]) res[u] = cand;
        }
        return res[u];
    }
}
