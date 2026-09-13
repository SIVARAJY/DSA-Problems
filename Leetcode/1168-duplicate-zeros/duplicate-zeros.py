class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        
        possible_dups = 0
        length = len(arr) - 1
        
        left = 0
        while left <= length - possible_dups:
            if arr[left] == 0:
                if left == length - possible_dups:
                    arr[length] = 0 
                    length -= 1
                    break
                possible_dups += 1
            left += 1
            
        last = length - possible_dups
        
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
