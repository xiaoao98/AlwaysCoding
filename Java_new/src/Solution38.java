public class Solution38 {
    public String countAndSay(int n) {
        if (n==1) {
            return String.valueOf(n);
        }
        StringBuilder output = new StringBuilder();
        String inputS = countAndSay(n-1);
        int num = 0;
        for (int i=0; i < inputS.length();i++) {
            if (i==0 || inputS.charAt(i) == inputS.charAt(i-1)) {
                num ++;
            }
            else if (inputS.charAt(i) != inputS.charAt(i-1)){
                output.append(num);
                output.append(inputS.charAt(i-1));
                num = 1;
            }
        }
        if (num != 0) {
            output.append(num);
            output.append(inputS.charAt(inputS.length()-1));
        }
        return output.toString();
    }

    public static void main(String[] args) {
        Solution38 solution = new Solution38();
        System.out.println(solution.countAndSay(4));
    }
}
