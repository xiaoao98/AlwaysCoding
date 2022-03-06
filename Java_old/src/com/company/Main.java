package com.company;

import com.sun.source.tree.Tree;

import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
}

class Solution {
    private char[][] board;
    int rowNum;
    int colNum;

    private boolean existHelper(String word, int index, int row, int col) {
        if (index == word.length()) {
            return true;
        }
        int[] rows = {-1, 1, 0, 0};
        int[] cols = {0, 0, -1, 1};
        if (row>=0 && row<this.rowNum && col>=0 && col< this.colNum && this.board[row][col] == word.charAt(index)) {
            this.board[row][col] = '#';
            for (int i=0; i<rows.length; i++) {
                if (existHelper(word, index+1, row+rows[i], col+cols[i])) {return true;}
            }
            this.board[row][col] = word.charAt(index);
        }
        return false;
    }

    public boolean exist(char[][] board, String word) {
        if (word.length() == 0) { return true;}
        if (board.length == 0) {return false;}
        this.board = board;
        this.rowNum = board.length;
        this.colNum = board[0].length;
        for (int i=0; i<board.length; i++){
            for (int j=0; j< board[0].length; j++) {
                if (existHelper(word, 0, i, j)) {return true;}
            }
        }
        return false;


    }
}

class Solution394 {
    private String decodingString;
    //    private ArrayList<Integer> openBracket;
    private int index = 0;

    public String decodeString(String s) {
        this.decodingString = s;
        this.index = 0;
        return decodeStringHelper();
    }

    private String decodeStringHelper() {
        StringBuilder decodedString = new StringBuilder(10);
        while (this.index < this.decodingString.length() && this.decodingString.charAt(this.index) != ']') {
            char ch = this.decodingString.charAt(this.index);
            if (Character.isLowerCase(ch)) {
                decodedString.append(ch);
                this.index++;
            }
            else if (Character.isDigit(ch)) {
                int startDigit = this.index;
                int endDigit = this.index;
                while (Character.isDigit(this.decodingString.charAt(endDigit))) {
                    endDigit += 1;
                }
                this.index = endDigit+1;
                String digitString = this.decodingString.substring(startDigit, endDigit);
                int repeatTime = Integer.parseInt(digitString);
                String repeatedString = decodeStringHelper();
                this.index += 1;
                decodedString.append(repeatedString.repeat(repeatTime));
            }
        }
        return decodedString.toString();
    }
}

public class Main {
    public static void characterTransfer(String input) {
        String[] inputArray = input.split("\n");
        StringBuilder output = new StringBuilder(100);
        for (String inputLine: inputArray) {
            String outputLine = lineTransfer(inputLine);
            output.append(outputLine);
            output.append("\n");
        }
        System.out.println(output);
    }

    private static String lineTransfer(String inputLine) {
        StringBuilder outputLine = new StringBuilder(10);
        String[] inputLineArray = inputLine.split("=");
        for (int i=0; i < inputLineArray[0].length(); i++) {
            char ch = inputLineArray[0].charAt(i);
            if (ch != '_') {
                outputLine.append(ch);
            } else {
                ch = inputLineArray[0].charAt(i+1);
                outputLine.append(Character.toUpperCase(ch));
                i++;
            }
        }
        outputLine.setLength(outputLine.length()-1);
        outputLine.append(":");
//        System.out.println(inputLineArray[1].split("\\(")[0].substring(10));
        switch (inputLineArray[1].split("\\(")[0].substring(10)) {
            case "Int": outputLine.append(" 123"); break;
            case "String": outputLine.append(" \"456\""); break;
            case "Date": outputLine.append(" \"2000-01-01\""); break;
            case "DateTime": outputLine.append(" \"2020-03-03T05:03:55Z\""); break;
            case "Boolean": outputLine.append(" true"); break;
            default: outputLine.append(" 111"); break;
        }
        return outputLine.toString();
    }

    public static void testCharacterEquals() {
        //primitive type uses == operator for equals comparasion
        char a1 = 'A';
        char a2 = 'A';
        if (a1 == a2) {
            System.out.println("primitive type comparasion: it's equal");
        }

        //From Java doc; The Character class wraps a value of the primitive type char in an object. An object of type Character contains a single field whose type is char.
        //Object type uses equals method for equals comparasion
        Character character1 = 'A';
        Character character2 = 'A';
        if (character1.equals(character2)) {
            System.out.println("object type comparasion: it's equal");
        }
    }

    private static int titleToNumber(String columnTitle) {
        int output = 0;
        int size = columnTitle.length();
        for (int i=0; i<size; i++) {
            output *= 26;
            char ch = columnTitle.charAt(i);
            output += ch - 'A' + 1;
        }
        return output;
    }

    public static ListNode sortList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }

        ListNode mid = findMid(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }

//    private static ListNode sortListHelper(ListNode head, ListNode tail) {
//
//    }

    private static ListNode findMid(ListNode head) {
        ListNode fast = head;
        ListNode slow = new ListNode(0, head);
        while ( fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode tmp = slow.next;
        slow.next = null;
        return tmp;
    }

    private static ListNode merge(ListNode left, ListNode right) {
        ListNode dummyhead = new ListNode();
        ListNode tail = dummyhead;
        while ( left != null && right != null) {
            if (left.val <= right.val) {
                tail.next = new ListNode(left.val);
                left = left.next;
                tail = tail.next;
            } else {
                tail.next = new ListNode(right.val);
                right = right.next;
                tail = tail.next;
            }
        }
        tail.next = (left == null)? right: left;
        return dummyhead.next;
    }

    public static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<List<Integer>>();
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        LinkedList<TreeNode> dequeue = new LinkedList<>();
        boolean isleftOrder = true;
        dequeue.add(root);
        dequeue.add(null);
        while (dequeue.size() != 0) {
            LinkedList<Integer> level = new LinkedList<>();
            while (dequeue.getFirst() != null) {
                TreeNode tmp = dequeue.removeFirst();
                if (isleftOrder) {
                    level.addLast(tmp.val);
                } else {
                    level.addFirst(tmp.val);
                }
                if ( tmp.left != null) dequeue.addLast(tmp.left);
                if ( tmp.right != null) dequeue.addLast(tmp.right);
            }
            dequeue.removeFirst();
            if (dequeue.size() > 0) dequeue.addLast(null);
            output.add(level);
            isleftOrder = ! isleftOrder;
        }
        return output;
    }

    public static TreeNode sortedArrayToBST(int[] nums) {
        return helperSortedArrayToBST(nums, 0, nums.length-1);
    }

    public static TreeNode helperSortedArrayToBST(int[] nums, int start, int end) {
        if (end < start) return null;
        if (end == start) return new TreeNode(nums[start]);
        int mid = start + (end-start) / 2;
        TreeNode left = helperSortedArrayToBST(nums, start, mid-1);
        TreeNode right = helperSortedArrayToBST(nums, mid+1, end);
        return new TreeNode(nums[mid], left, right);
    }

    public static int hammingWeight(int n) {
//        String a = Integer.toBinaryString(n);
//        int output = 0;
//        for (int i=0; i < a.length(); i++) {
//            if (a.charAt(i) == '1'){
//                output ++;
//            }
//        }
//        return output;
        int sum = 0;
        int mask = 1;
        for (int i=0; i<32; i++) {
            if ((n & mask) != 0) {
                sum += 1;
            }
            mask <<= 1;
        }
        return sum;
    }

    public static void main(String[] args) {
        String input =
                "    patient_serial_number = graphene.Int(required=True)\n" +
                        "    patient_full_name = graphene.String(required=True)\n" +
                        "    patient_birthday = graphene.Date(required=True)\n" +
                        "    date_of_admission = graphene.DateTime(required=True)\n" +
                        "    mother_card_number = graphene.Int(required=True)\n" +
                        "    gravidae = graphene.Int(required=True)\n" +
                        "    parity = graphene.Int(required=True)\n" +
                        "    gestation = graphene.Int(required=True)\n" +
                        "    diagnosis_complications = graphene.String(required=True)\n" +
                        "    uterotonic_for_pph = graphene.String(required=True)\n" +
                        "    hb = graphene.Int(required=True)\n" +
                        "    partograph_used = graphene.Boolean(required=True)\n" +
                        "    delivery_date_time = graphene.Date(required=True)\n" +
                        "    delivery_place = graphene.String(required=True)\n" +
                        "    birth_notification_number = graphene.Int(required=True)\n" +
                        "    presentation = graphene.String(required=True)\n" +
                        "    mode_of_delivery = delivery_place = graphene.String(required=True)\n" +
                        "    apgar_score_appearance = graphene.Int(required=True)\n" +
                        "    apgar_score_pulse = graphene.Int(required=True)\n" +
                        "    apgar_score_grimace = graphene.Int(required=True)\n" +
                        "    apgar_score_activity = graphene.Int(required=True)\n" +
                        "    apgar_score_respiration = graphene.Int(required=True)\n" +
                        "    apgar_score_total = graphene.Int(required=True)\n" +
                        "    breastfed_within_hour = graphene.Boolean(required=True)\n" +
                        "    delivery_conducted_by_name_1 = graphene.String(required=True)\n" +
                        "    delivery_conducted_by_designation_1 = graphene.String(required=True)\n" +
                        "    delivery_conducted_by_name_2 = graphene.String(required=True)\n" +
                        "    delivery_conducted_by_designation_2 = graphene.String(required=True)\n" +
                        "    baby_alive = graphene.String(required=True)\n" +
                        "    baby_dead = graphene.String(required=True)\n" +
                        "    congenital_abnormality = graphene.Boolean(required=True)\n" +
                        "    baby_sex = graphene.String(required=True)\n" +
                        "    baby_weight = graphene.Int(required=True)\n" +
                        "    placenta_completely_expelled = graphene.Boolean(required=True)\n" +
                        "    bcg = graphene.Date(required=True)\n" +
                        "    opv = graphene.Date(required=True)\n" +
                        "    vitamin_a = graphene.Boolean(required=True)\n" +
                        "    hiv_positive_prior = graphene.Boolean(required=True)\n" +
                        "    hiv_counselled = graphene.Boolean(required=True)\n" +
                        "    hiv_tested = graphene.Boolean(required=True)\n" +
                        "    hiv_results = graphene.String(required=True)\n" +
                        "    art_prophylaxis_mother = graphene.Boolean(required=True)\n" +
                        "    art_prophylaxis_infant = graphene.Boolean(required=True)\n" +
                        "    discharge_date = graphene.Date(required=True)\n" +
                        "    days_of_stay = graphene.Int(required=True)\n" +
                        "    discharge_condition_mother = graphene.String(required=True)\n" +
                        "    discharge_condition_baby = graphene.String(required=True)\n" +
                        "    iycf = graphene.Boolean(required=True)\n" +
                        "    general_counselling = graphene.Boolean(required=True)\n" +
                        "    vital_statistics_notifications_code = graphene.Int(required=True)\n" +
                        "    next_visit_date = graphene.DateTime(required=True)\n" +
                        "    mother_referred_from_another_facility = graphene.Boolean(required=True)\n" +
                        "    mother_referred_to_another_facility = graphene.Boolean(required=True)\n" +
                        "    infant_referred_to_another_facility = graphene.Boolean(required=True)\n" +
                        "    remarks = graphene.String(required=True)\n" +
                        "    chw_has_followed_up = graphene.Boolean()\n" +
                        "    patient_id = graphene.ID(required=True)\n";
        characterTransfer(input);
//        Solution394 solution = new Solution394();
//        System.out.println(solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"));
//        Solution solution = new Solution();
//        System.out.println(solution.exist(new char[][]{{'A','B','C','E'}, {'S','F','C','S'},{'A','D','E','E'}}, "ABCCED"));
//        System.out.println(hammingWeight(-3));
//        testCharacterEquals();
//        System.out.println("Hello LeetCode");
//        int output = titleToNumber("ZY");
//        ListNode a = new ListNode(1);
//        ListNode b = new ListNode(2);
//        ListNode c = new ListNode(3);
//        ListNode d = new ListNode(4);
//        d.next = b;
//        b.next = a;
//        a.next = c;
//        ListNode e = sortList(d);
//        System.out.println(output);
    }
}
