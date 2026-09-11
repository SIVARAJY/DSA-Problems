class Solution {
    public int hammingDistance(int x, int y) {
        int cnt=0;
        int z = x^y;
        String s = Integer.toBinaryString(z);
        int h = s.length();
        while(h-- > 0){
            if(s.charAt(h)=='1'){
                cnt++;
            }
        }
        return cnt;
    }
}