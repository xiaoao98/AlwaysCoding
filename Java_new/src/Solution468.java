public class Solution468 {
    public String validIPAddress(String queryIP) {
        if (queryIP.length() == 0) {
            return "Neither";
        }
        if (queryIP.charAt(0) == ':' || queryIP.charAt(0) == '.'
                || queryIP.charAt(queryIP.length()-1) == ':' || queryIP.charAt(queryIP.length()-1) == '.') {
            return "Neither";
        }
        String[] tmpArray = queryIP.split("\\.");
        boolean flag = true;
        if (tmpArray.length == 4) {
            for (String tmp: tmpArray) {
                if (tmp.length() == 0 || (tmp.charAt(0) == '0' && tmp.length()>1)) {
                    flag = false;
                    break;
                }
                int tmpvalue = 0;
                for (int i=0; i<tmp.length(); i++) {
                    if (!Character.isDigit(tmp.charAt(i))) {
                        flag = false;
                        break;
                    }
                    tmpvalue = tmpvalue * 10 + tmp.charAt(i)-'0';
                    if (tmpvalue > 255) {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag){return "IPv4";}
        }

        tmpArray = queryIP.split(":");
        flag = true;
        if (tmpArray.length == 8) {
            for (String tmp: tmpArray) {
                if (tmp.length() < 1 || tmp.length() > 4) {
                    flag = false; break;
                }
                for (int i=0; i<tmp.length(); i++) {
                    if (!Character.isDigit(tmp.charAt(i))
                            && (tmp.charAt(i) < 'A'
                            || (tmp.charAt(i) > 'F' && tmp.charAt(i) < 'a')
                            || tmp.charAt(i) > 'f') ){
                        flag = false; break;
                    }
                if (!flag) {break;}
                }
            }
            if (flag) {return "IPv6";}
        }
        return "Neither";
    }

    public static void main(String[] args) {
        Solution468 solution = new Solution468();
        System.out.println(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"));
    }
}


