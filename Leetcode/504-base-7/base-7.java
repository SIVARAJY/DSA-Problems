class Solution {
    public String convertToBase7(int num) {
        if(num==0) return "0";
        int f=0;
        if(num<0){
            f = 1;
            num=-num;
        }
        Stack<Integer> st = new Stack<>();
        StringBuilder s = new StringBuilder();
        while(num>0){
            st.push(num%7);
            num/=7;
        }
        if(f==1) s.append("-");
        while(!st.isEmpty()){
            s.append(st.pop());
        }
        return s.toString();
    }
}