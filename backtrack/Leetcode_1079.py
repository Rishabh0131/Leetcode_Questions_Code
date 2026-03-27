class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        tiles = sorted(tiles)  # type: ignore

        used = [False] * len(tiles)

        def backtrack():

            count = 0

            for i in range(len(tiles)):

                if used[i]:
                    continue

                if i > 0 and tiles[i - 1] == tiles[i] and not used[i - 1]:
                    continue

                used[i] = True
                count += 1

                count += backtrack()
                used[i] = False

            return count

        return backtrack()
