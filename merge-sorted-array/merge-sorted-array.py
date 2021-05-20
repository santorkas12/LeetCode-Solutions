class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        
        nums1.sort()
        
        return nums1
            
            
#         if not nums1:
#             return nums2
#         if not nums2:
#             return nums1
        
#         index_f0 = m+n//2
        
#         point1 = 0
        
#         while point1 < index_f0:
#             if nums2[0] < nums1[point1]:
#                 nums1.insert(point1, nums2[0])
                
#                 del nums2[0]
#                 nums1.pop()
                
#                 if not nums2:
#                     break
#             else:
#                 point1 += 1

#         if len(nums2) == n:
#             nums1[index_f0-1:] = nums2
#         elif nums2:
#             nums1[index_f0:] = nums2
                
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        