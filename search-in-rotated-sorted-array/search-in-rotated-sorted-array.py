class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                #Focus on local recursion between original start and new mid
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                #Change start to focus on right half of array    
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
        
        
# Binary search solution - but linearithmic time complexity - n log(n)

#         n = len(nums)
        
#         rmin = nums.index(min(nums))
#         rmax = n-1
#         lmin = 0
#         lmax = rmin-1

        
#         #use left sorted if this 
        
#         if target in nums:
#             if target > nums[rmax]:
#                 while lmin <= lmax:
#                     guess = (lmin+lmax)//2

#                     if target > nums[guess]:
#                         lmin = guess+1
#                     elif target < nums[guess]:
#                         lmax = guess-1
#                     else:
#                         return guess


#             #use right sorted if this
#             elif target < nums[rmax]:
#                 while rmin <= rmax:
#                     guess = (rmin+rmax)//2

#                     if target > nums[guess]:
#                         rmin = guess + 1
#                     elif target < nums[guess]:
#                         rmax = guess - 1
#                     else:
#                         return guess         

#             else:
#                 return rmax
#         else:
#             return -1

        
        
        
        
        
        
        
        
#Linear search is super easy
#         n = len(nums)
        
#         for i in range(n):
#             if nums[i] == target:
#                 return i
            
#         return -1