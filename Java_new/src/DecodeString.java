import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class DecodeString {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i=0; i<s.length(); i++) {
            char tmp = s.charAt(i);
            if (tmp != ']') {
                stack.add(tmp);
            }
            else {
                List<Character> tmp2 = new ArrayList<>();
                while(stack.peek() != '[') {
                    tmp2.add(stack.pop());
                }
                stack.pop();
                int repeat = 0, base = 1;
                while(!stack.isEmpty() && Character.isDigit(stack.peek())) {
                    repeat = (stack.pop()-'0') * base + repeat;
                    base *= 10;
                }
                // int repeat = Integer.parseInt(String.valueOf(stack.pop()));
                while (repeat!=0) {
                    for (int j=tmp2.size()-1; j>=0; j--) {
                        stack.push(tmp2.get(j));
                    }
                    repeat--;
                }
            }
        }
        char[] output = new char[stack.size()];
        for (int i=stack.size()-1; i>=0; i--) {
            output[i] = stack.pop();
        }
        return new String(output);
    }
}
