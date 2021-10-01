class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        num_set = set()
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                return True
            
        return False
        
        
        

#         set_nums = set(nums)
        
#         if len(set_nums) == len(nums):
#             return False
#         else:
#             return True