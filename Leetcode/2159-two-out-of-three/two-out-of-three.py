class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dicto={}
        ans=[]
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        for i in range(len(nums1)):
            dicto[nums1[i]]=dicto.get(nums1[i],0)+1
        for i in range(len(nums2)):
            dicto[nums2[i]]=dicto.get(nums2[i],0)+1
        for i in range(len(nums3)):
            dicto[nums3[i]]=dicto.get(nums3[i],0)+1
        for itm,cnt in dicto.items():
            if(cnt>=2):
                ans.append(itm)
        return ans
