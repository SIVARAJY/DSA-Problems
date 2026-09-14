class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        for char in columnTitle:
            value = ord(char) - 64
            column_number = column_number * 26 + value
        return column_number
