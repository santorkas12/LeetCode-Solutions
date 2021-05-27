class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lpref = ''
        
        if not strs:
            return lpref
        
        if len(strs) == 1:
            lpref = strs[0]
            return lpref
        
        shortest = min(strs, key = len)
        n = len(shortest)
        
        if n == 0:
            return lpref
        
        for i in range(n):
            for word in strs:
                if shortest[i] != word[i]:
                    return lpref
                else:
                    continue
            
            lpref += shortest[i]
        
        return lpref
    
        