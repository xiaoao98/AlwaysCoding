import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class LetterCombinationsofaPhoneNumber {
    private List<String> combinations;
    private HashMap<Character, String> dic;
    public List<String> letterCombinations(String digits) {
        combinations = new ArrayList<>();
        if (digits.equals("")) return combinations;
        dic = new HashMap<>();
        dic.put('2', "abc");
        dic.put('3', "def");
        dic.put('4', "ghi");
        dic.put('5', "jkl");
        dic.put('6', "mno");
        dic.put('7', "pqrs");
        dic.put('8', "tuv");
        dic.put('9', "wxyz");
        backtrack(digits, new StringBuilder(""));
        return combinations;
    }
    public void backtrack(String digits, StringBuilder comb) {
        if (digits.length() == 0) {combinations.add(comb.toString());return;}
        for (char ch: dic.get(digits.charAt(0)).toCharArray()) {
            backtrack(digits.substring(1), comb.append(ch));
            comb.deleteCharAt(comb.length()-1);
        }
    }

}
