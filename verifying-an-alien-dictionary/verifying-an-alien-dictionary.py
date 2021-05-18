class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_index = {}
                    
        for i, v in enumerate(order):
            dict_index[v] = i
            
        for a, b in zip(words, words[1:]): #Loop through current and next simultaneously
            #if a is longer than b and a is identical to b up to its length, then b should be before a
            if len(a) > len(b) and a[:len(b)] == b:
                return False
        
            #Once the length has been verified, we then check character by character
            
            for char_1, char_2 in zip(a, b):
                if dict_index[char_1] < dict_index[char_2]:
                    break
                elif dict_index[char_1] > dict_index[char_2]:
                    return False
                        
        return True
