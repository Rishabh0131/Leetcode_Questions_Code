class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        left = 0
        res = k
        recolor = 0
        n = len(blocks)

        for right in range(n):
            if blocks[right] == "W":
                recolor += 1
            if (right - left) + 1 == k:
                res = min(res, recolor)
                if blocks[left] == "W":
                    recolor -= 1
                left += 1

        return res
