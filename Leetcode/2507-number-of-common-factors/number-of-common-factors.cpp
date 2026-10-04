class Solution {
public:
    int commonFactors(int a, int b) {
        int m;
        if(a>b){
            m=a;
        }
        else if(b>a){
            m=b;
        }
        int count=0;
        for(int i=1;i<=m;i++){
            if(a%i==0 && b%i==0){
                count++;
            }
        }
        return count;
    }
};