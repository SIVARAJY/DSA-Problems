class Solution {
    public int ladderLength(String n, String s, List<String> wl) {
        Set<String> st = new HashSet<>();
        Queue<String> qu = new ArrayDeque<>();
        int f = 0;
        for(String word: wl)
            {
                if(word.compareTo(s)==0)
                    f = 1;
                st.add(word);
            }

        if(f==0) return 0;
        qu.offer(n);
        int lev = 0;
        int lsize = 0;
        while(!qu.isEmpty()){
            lev++;
            lsize = qu.size();
            while(lsize-- > 0){
            String curr=qu.poll();
            for(int i=0;i<curr.length();i++){
                StringBuffer temp = new StringBuffer(curr);
                for(char ch = 'a';ch<= 'z';ch++){
                    temp.setCharAt(i,ch);
                    String w = temp.toString();
                    if(w.equals(s)) return lev+1;
                    if(w.compareTo(curr)==0) continue;
                    if(st.contains(w)){
                        qu.offer(w);
                        st.remove(w);
                    }
                    

                }
            }
        }
    }
    return 0;
    }
}    
