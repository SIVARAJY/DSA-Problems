class Solution {
    public int[] scoreValidator(String[] events) {
        int[] res = new int[2];
        for (String s : events) {
            char c = s.charAt(s.length() - 1);
            if (c == 'D' || c == 'B') {
                res[0]++;
            } else if (c == 'W') {
                res[1]++;
                if (res[1] == 10) {
                    break;
                }
            } else {
                res[0] += c - '0';
            }
        }
        return res;
    }
}