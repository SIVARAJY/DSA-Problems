import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        is_valid = re.compile(r'^([a-z]+(-[a-z]+)?)?[!.,]?$').match
        
        return len([token for token in sentence.split() if is_valid(token)])
