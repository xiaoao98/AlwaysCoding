import java.util.*;

public class Solution819 {
    public String mostCommonWord(String paragraph, String[] banned) {
        HashSet<String> bannedWords = new HashSet<>();
        HashMap<String, Integer> counts = new HashMap<>();
        for (String bannedword: banned) {
            bannedWords.add(bannedword);
        }
        for (String word: paragraph.replaceAll("[^a-zA-Z]", " ").toLowerCase().split("\\s+")) {
            if (!bannedWords.contains(word)) {
                counts.put(word, counts.getOrDefault(word, 0)+1);
            }
        }
        String result = "";
        for (String countWord: counts.keySet()) {
            if (result.equals("") || counts.get(result)<counts.get(countWord)) {
                result = countWord;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution819 solution819 = new Solution819();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        String c = "142342";
        c = c.replaceAll("1", "3");
        StringBuilder a = new StringBuilder(c);
        a.reverse();
        System.out.println(a);
        Map<String, Integer> unsortMap = new HashMap<>();
        unsortMap.put("B", 55);
        unsortMap.put("D", 20);
        unsortMap.put("A", 20);
        unsortMap.put("C", 70);
        List<Map.Entry<String, Integer>> infoIds = new ArrayList<>(unsortMap.entrySet());
        infoIds.sort((o1, o2) -> (o1.getValue().compareTo(o2.getValue()) == 0) ?
                o1.getKey().compareTo(o2.getKey()) : o1.getValue().compareTo(o2.getValue()));
        System.out.println(infoIds);
        int b = (int)Math.pow(2, 5);
        System.out.println(b);
        StringBuilder B = new StringBuilder();
        B.append('3');
        B.append("234");
        B.deleteCharAt(a.length()-1);
        System.out.println(B);
        int A = 93;
        String aa = String.valueOf(A);
        A = Integer.parseInt(aa);
        System.out.println(a+"1");
        System.out.println(A+1);
        String paragraph = "  Bob hit a ball, the hit BALL flew far after it was hit.  ";
        char[] pp= paragraph.toCharArray();
        String p = new String(pp);
        System.out.println(pp[2]);
        System.out.println(p);
        int AA = 152;
        String aaa = Integer.toBinaryString(A);
        int AAA = Integer.parseInt(aaa, 2);
        System.out.println(a);
        System.out.println(AAA);
        int[] aaaa = {1, 4, 2, 5};
        ArrayList<Integer> AAAA = new ArrayList<>(Arrays.asList(aaaa[0], aaaa[1], aaaa[2], aaaa[3]));
//        for (int i: a) {
//            A.add(i);
//        }
        Collections.sort(AAAA);
        System.out.println(AAAA.get(1));
        System.out.println(paragraph.indexOf("hitt"));
        System.out.println(paragraph.stripLeading());
        System.out.println(paragraph.stripTrailing());
        System.out.println(solution819.mostCommonWord(paragraph, new String[] {"hit"}));
    }
}
