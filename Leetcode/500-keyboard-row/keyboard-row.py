class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = {'q','w','e','r','t','y','u','i','o','p'}
        l2 = {'a','s','d','f','g','h','j','k','l'}
        l3 = {'z','x','c','v','b','n','m'}
        result=[]
        for word in words:
            new = set(list(word.lower()))
            one = new & l1
            two = new & l2
            three = new & l3

            if (one == new) or (two==new) or (three==new) : 
                    result.append(word)
        return result        

                
        