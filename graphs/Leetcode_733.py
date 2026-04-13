from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        visited = set()

        originalColor = image[sr][sc]

        def recolor(i, j):

            nonlocal originalColor

            if (
                i < 0
                or j < 0
                or i >= len(image)
                or j >= len(image[0])
                or image[i][j] != originalColor
                or (i, j) in visited
            ):
                return

            visited.add((i, j))

            image[i][j] = color

            recolor(i + 1, j)
            recolor(i - 1, j)
            recolor(i, j + 1)
            recolor(i, j - 1)

        recolor(sr, sc)

        return image
