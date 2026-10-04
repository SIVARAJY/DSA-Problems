class Solution {
    public boolean checkValidString(String s) {
        int openMin = 0;
        int openMax = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                openMin++;
                openMax++;
            } else if (c == ')') {
                openMin--;
                openMax--;
            } else if (c == '*') {
                openMin--; 
                openMax++; 
            }

            if (openMax < 0) {
                return false;
            }

            if (openMin < 0) {
                openMin = 0;
            }
        }

        return openMin == 0;
    }
}
