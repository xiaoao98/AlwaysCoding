import java.util.LinkedList;
import java.util.List;

public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        return generateParenthesis(n, n);
    }

    public List<String> generateParenthesis(int p, int q) {
        List<String> outputs = new LinkedList<>();
        if (p == 0 && q == 0) {
            outputs.add("");
        }
        if (p!=0 || q!= 0) {
            if (p < q) {
                for (String output: generateParenthesis(p, q-1)) {
//                    StringBuilder tmp = new StringBuilder();
//                    tmp.append(")");
//                    tmp.append(output);
                    outputs.add(")"+output);
                }
            }
            if (p>0) {
                for (String output: generateParenthesis(p-1, q)) {
                    outputs.add("("+output);
//                    System.out.println(output);
                }
            }
        }
        return outputs;
    }

    public static void main(String[] args) {
        GenerateParentheses solution = new GenerateParentheses();
        System.out.println(solution.generateParenthesis(3));
    }
}
