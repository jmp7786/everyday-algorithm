import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return new ArrayList<>();
        }

        Map<Character, char[]> map = new HashMap<>();
        map.put('2', new char[]{'a', 'b', 'c'});
        map.put('3', new char[]{'d', 'e', 'f'});
        map.put('4', new char[]{'g', 'h', 'i'});
        map.put('5', new char[]{'j', 'k', 'l'});
        map.put('6', new char[]{'m', 'n', 'o'});
        map.put('7', new char[]{'p', 'q', 'r', 's'});
        map.put('8', new char[]{'t', 'u', 'v'});
        map.put('9', new char[]{'w', 'x', 'y', 'z'});

        List<String> result = new ArrayList<>();
        backtrack(result, new StringBuilder(), digits, map, 0);
        return result;
    }

    private void backtrack(List<String> result, StringBuilder current, String digits, Map<Character, char[]> map, int index) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        char digit = digits.charAt(index);
        char[] chars = map.get(digit);
        for (char c : chars) {
            current.append(c);
            backtrack(result, current, digits, map, index + 1);
            current.deleteCharAt(current.length() - 1);
        }
    }

}
