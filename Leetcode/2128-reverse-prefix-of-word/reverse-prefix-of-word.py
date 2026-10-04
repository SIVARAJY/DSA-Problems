class Solution(object):
    def reversePrefix(self, word, ch):
        end_index = word.find(ch)
        
        if end_index == -1:
            return word
        
        return word[end_index::-1] + word[end_index+1:]
