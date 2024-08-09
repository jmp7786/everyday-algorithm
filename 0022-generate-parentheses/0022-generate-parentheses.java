class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        List<Character> path = new ArrayList<>();
        path.add('(');
        generate(1, 0, n, path, result);        
        return result;
    }

    private void generate(int left, int right, int n, List<Character> path, List<String> result) {
        if (left + right == n * 2) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < path.size(); i++) {
                sb.append(path.get(i));
            }
            result.add(sb.toString());
            
        }

        if (left < n) {
            path.add('(');
            generate(left + 1, right, n, path, result);
            path.removeLast();
        }

        if (right < left) {
            path.add(')');
            generate(left, right + 1, n, path, result);
            path.removeLast();
        }
    }
}
