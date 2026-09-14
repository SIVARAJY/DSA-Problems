class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Use sets for O(1) lookup times
        l1 = set('qwertyuiop')
        l2 = set('asdfghjkl')
        l3 = set('zxcvbnm')
        
        result = []
        
        for word in words:
            # Convert the word characters into a set
            word_set = set(word.lower())
            
            # Check if the word's characters are a subset of any single row
            if word_set.issubset(l1) or word_set.issubset(l2) or word_set.issubset(l3):
                result.append(word)
                
        return result
