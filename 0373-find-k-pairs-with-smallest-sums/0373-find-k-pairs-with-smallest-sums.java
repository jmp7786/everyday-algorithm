import java.util.PriorityQueue;
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> que = new PriorityQueue<>((a, b) -> a[0] + a[1] - b[0] - b[1]);
        List<List<Integer>> res = new ArrayList<>();
        if (nums1.length == 0 || nums2.length == 0 || k == 0) return res;

        for (int i = 0; i < nums1.length && i < k; i++) {
            que.offer(new int[] { nums1[i], nums2[0], 0 });
        }

        while (k-- > 0 && !que.isEmpty()) {
            int[] cur = que.poll();
            List<Integer> pair = new ArrayList<>();
            pair.add(cur[0]);
            pair.add(cur[1]);
            res.add(pair);

            if (cur[2] == nums2.length - 1) continue;
            que.offer(new int[] { cur[0], nums2[cur[2] + 1], cur[2] + 1 });
        }

        return res;
    }
}
