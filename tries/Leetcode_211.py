class TrieNode:

    def __init__(self) -> None:

        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        curr = self.root

        for ch in word:

            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(i, root):

            curr = root

            for j in range(i, len(word)):

                ch = word[j]

                if ch == ".":

                    for child in curr.children.values():

                        if dfs(j + 1, child):
                            return True

                    return False

                else:

                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]

            return curr.is_end

        return dfs(0, self.root)
