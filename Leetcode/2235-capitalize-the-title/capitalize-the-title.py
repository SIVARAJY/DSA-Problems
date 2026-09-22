class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        l = title.split(" ")
        for i in range(len(l)):
            if len(l[i])>2:
                l[i]=l[i].capitalize()
        return " ".join(l) 