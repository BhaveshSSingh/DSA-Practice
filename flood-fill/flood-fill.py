class Solution(object):
    def floodFill(self, img, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        col = img[sr][sc]
        if col == newColor:
            return img              
        img[sr][sc] = newColor
        if sr > 0 and col == img[sr-1][sc]:
            self.floodFill(img,sr-1,sc,newColor)
        if sr < len(img)-1  and col == img[sr+1][sc]:
            self.floodFill(img,sr+1,sc,newColor)
        if sc > 0 and col == img[sr][sc-1]:
            self.floodFill(img,sr,sc-1,newColor)
        if sc < len(img[0])-1 and col == img[sr][sc+1]:
            self.floodFill(img,sr,sc+1,newColor)
        return img