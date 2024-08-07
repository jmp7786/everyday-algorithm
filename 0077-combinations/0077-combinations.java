class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        findCombinations(1, n, k, new ArrayList<>(), result);
        return result;
    }

    private void findCombinations(int start, int end, int k, List<Integer> path, List<List<Integer>> result) {
        for(int i = start; i <= end; i++) {
            path.add(i);
            int size = path.size();
            if (size == k) {
                result.add(new ArrayList<>(path));
            } else {
                findCombinations(i+1, end, k, path, result);
            }
            path.removeLast();
        }
    }


}