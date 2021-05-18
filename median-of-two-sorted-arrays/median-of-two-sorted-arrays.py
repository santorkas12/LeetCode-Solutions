import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        joinedlist = nums1 + nums2
        joinedlist.sort()
        
        n = len(joinedlist)
        
        
        if n % 2 == 0:
            median = ((joinedlist[int((n/2)-1)]) + (joinedlist[int((n/2))])) / 2
        else:
            median = joinedlist[int((n+1)/2)-1]
            
        return median
        