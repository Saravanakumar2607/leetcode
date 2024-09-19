class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
       
        pointer1, pointer2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        
        while pointer1 < len1 and pointer2 < len2:
            if nums1[pointer1] == nums2[pointer2]:
                return nums1[pointer1]
            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1
        
        return -1
