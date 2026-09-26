class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {key: value for key, value in knowledge}
        
        result = []
        current_key = []
        is_inside_bracket = False
        
        for char in s:
            if char == '(':
                is_inside_bracket = True
            elif char == ')':
                is_inside_bracket = False
                key_str = "".join(current_key)
                result.append(mapping.get(key_str, "?"))
                current_key = []
            else:
                if is_inside_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)
