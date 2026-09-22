class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = coordinate1[0], coordinate1[1]
        x2, y2 = coordinate2[0], coordinate2[1]
        x_diff = abs(ord(x1) - ord(x2))
        y_diff = abs(ord(y1) - ord(y2))

        return (x_diff & 1) == (y_diff & 1)