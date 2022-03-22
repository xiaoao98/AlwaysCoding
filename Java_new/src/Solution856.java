import java.util.Stack;

public class Solution856 {
    public int scoreOfParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
//        for (int i=0; i<s.length(); i++) {
//            if (s.charAt(i)=='(') {
//                stack.add("(");
//            }
//            if (s.charAt(i)==')') {
//                String tmp = stack.pop();
//                int tmpValue = 0;
//                while (!tmp.equals("(")) {
//                    tmpValue += Integer.parseInt(tmp);
//                    tmp = stack.pop();
//                }
//                if ( tmpValue==0 ) {
//                    stack.add("1");
//                }
//                else {
//                    stack.add(String.valueOf(tmpValue*2));
//                }
//            }
//        }
//        int output = 0;
//        while ( !stack.isEmpty()) {
//            output+=Integer.parseInt(stack.pop());
//        }
//        return output;
        stack.push(0);
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(0);  //depth++
            }
            else {
                int tmp1 = stack.pop();  //value of this depth
                int tmp2 = stack.pop(); //value of the last depth
                stack.push(tmp2+Math.max(tmp1*2, 1));
            }
        }
        return stack.pop();
    }
}
