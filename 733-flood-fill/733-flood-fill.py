class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        col = image[sr][sc]
        if col == newColor:
            return image
        image[sr][sc] =newColor
        if sc > 0 and image [sr][sc-1] ==col:
            self.floodFill(image,sr,sc-1,newColor)
        if sc < len(image[0])-1 and image [sr][sc+1] ==col:
            self.floodFill(image,sr,sc+1,newColor)
        if sr > 0 and image [sr-1][sc] ==col:
            self.floodFill(image,sr-1,sc,newColor)
        if sr < len(image)-1 and image [sr+1][sc] ==col:
            self.floodFill(image,sr+1,sc,newColor)
        return image 