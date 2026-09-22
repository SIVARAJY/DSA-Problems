class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col,row=list(coordinates)[0],list(coordinates)[1]
        if(col=="a" or col=="c" or col=="e" or col=="g") and int(row)%2==1:
            return False
        if(col=="b" or col=="d" or col=="f" or col=="h") and int(row)%2==0:
            return False
        return True    

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        if (self.squareIsWhite(coordinate1) and self.squareIsWhite(coordinate2)) or (not self.squareIsWhite(coordinate1) and not self.squareIsWhite(coordinate2)):
            return True
        return False    