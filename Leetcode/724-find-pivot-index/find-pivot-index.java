class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;

        if(n==1) return 0;

        //declaration prefixsum and suffixsum arrays
        int[] pres = new int[n];
        int[] sufs = new int[n];

        //Initializing first element of pres and last element of sufs
        pres[0]=nums[0];
        sufs[n-1]=nums[n-1];

        //prefix sum and suffixsum for loop
        for(int i=1;i<n;i++) pres[i]=pres[i-1]+nums[i];
        for(int i=n-2;i>=0;i--) sufs[i]=sufs[i+1]+nums[i];
        
        //checking each element to find pivot index
        for(int i=0;i<n;i++){
            if(i==0 && sufs[i+1]==0) return i;
            else if(i>0 && i<n-1 && pres[i-1]==sufs[i+1]) return i;
            else if(i==n-1 && pres[i-1]==0) return i;
        }
        return -1;
    }
}