class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        hold_dict = {}
        
        for i in range(n):
            value = target-nums[i]
            
            if value in hold_dict:
                return [i, hold_dict[value]]
            
            else:
                hold_dict[nums[i]] = i
            
        
        
        
        
#         n = len(nums)
        
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:                
#                     return [i, j]
        