class Solution(object):
    def addedInteger(self, nums1, nums2):
        n = sum(nums1)
        m =sum(nums2)
        return (m-n)//len(nums1)
        