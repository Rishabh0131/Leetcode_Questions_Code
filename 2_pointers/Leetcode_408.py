class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordPtr = 0
        abbrPtr = 0

        while wordPtr < len(word) and abbrPtr < len(abbr):
            if abbr[abbrPtr].isdigit():
                if abbr[abbrPtr] == "0":
                    return False

                num = 0
                while abbrPtr < len(abbr) and abbr[abbrPtr].isdigit():
                    num = num * 10 + int(abbr[abbrPtr])
                    abbrPtr += 1
                wordPtr += num
            else:
                if wordPtr >= len(word) or word[wordPtr] != abbr[abbrPtr]:
                    return False
                wordPtr += 1
                abbrPtr += 1

        return wordPtr == len(word) and abbrPtr == len(abbr)
