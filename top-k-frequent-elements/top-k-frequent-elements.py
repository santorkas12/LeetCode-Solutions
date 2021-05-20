class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}
        
        for item in nums:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
                
        result = []
        
        while k > 0:
            max_key = max(count_dict, key = count_dict.get)
            result.append(max_key)
            del count_dict[max_key]
            k -= 1
                              
        return result