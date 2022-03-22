import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class Solution1249 {
    class Solution {
        public String minRemoveToMakeValid(String s) {
            StringBuilder output = new StringBuilder();
            Stack<Integer> bracket = new Stack<>();
            Set<Integer> remove = new HashSet<>();
            for (int i=0; i<s.length(); i++) {
                if (s.charAt(i) == '(') {
                    bracket.push(i);
                }
                if (s.charAt(i) == ')') {
                    if (bracket.isEmpty()) {
                        remove.add(i);
                    }
                    else {
                        bracket.pop();
                    }
                }
            }
            while (!bracket.isEmpty()) {
                remove.add(bracket.pop());
            }
            for (int i=0; i<s.length(); i++) {
                if (!remove.contains(i)) {
                    output.append(s.charAt(i));
                }
            }
            return output.toString();

        }
    }
}
