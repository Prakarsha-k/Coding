import java.util.*;

class Solution {
    public boolean isNStraightHand(int[] hand, int W) {
        if (hand.length % W != 0) return false;
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for (int h : hand) map.put(h, map.getOrDefault(h, 0) + 1);
        
        while (!map.isEmpty()) {
            int first = map.firstKey();
            for (int i = 0; i < W; i++) {
                int key = first + i;
                if (!map.containsKey(key)) return false;
                map.put(key, map.get(key) - 1);
                if (map.get(key) == 0) map.remove(key);
            }
        }
        return true;
    }
}
