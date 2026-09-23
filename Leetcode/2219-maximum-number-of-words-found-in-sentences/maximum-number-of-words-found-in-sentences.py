class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxe=0
        for i in sentences:
            l = i.split(" ")
            maxe=max(maxe,len(l))

        return maxe       