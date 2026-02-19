class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        map1 = {}
        map2 = {}
        left = 0

        k = len(s1)

        for ch in s1:
            map1[ch] = 1 + map1.get(ch, 0)

        for right in range(len(s2)):
            map2[s2[right]] = 1 + map2.get(s2[right], 0)

            if right - left + 1 > k:
                map2[s2[left]] -= 1

                if map2[s2[left]] == 0:
                    map2.pop(s2[left])
                left += 1

            if right - left + 1 == k:
                if map1 == map2:
                    return True

        return False
