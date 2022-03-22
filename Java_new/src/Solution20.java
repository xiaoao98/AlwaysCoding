import java.util.LinkedList;

public class Solution20 {
    public boolean isValid(String s) {
        LinkedList<Character> bracket = new LinkedList<>();
        for (int i=0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case '(': bracket.add('('); break;
                case ')':
                    if (!bracket.removeLast().equals(')')) {return false;}
                case '[': bracket.add('['); break;
                case ']':
                    if (!bracket.removeLast().equals(']')) {return false;}
                case '{': bracket.add('{'); break;
                case '}':
                    if (!bracket.removeLast().equals('}')) {return false;}
            }
        }
        return bracket.isEmpty();
    }
}
