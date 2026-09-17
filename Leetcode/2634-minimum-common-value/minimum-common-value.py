class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        r = 0
        while l < len(nums1):
            if nums1[l] > nums2[len(nums2) - 1]:
                return -1
            if nums2[r] > nums1[len(nums1) - 1]:
                return -1 
            if nums1[l] == nums2[r]:
                return nums1[l]
            # l < r
            if nums1[l] < nums2[r]:
                l += 1
            # l > r
            if nums1[l] > nums2[r]:
                r += 1
        return -1