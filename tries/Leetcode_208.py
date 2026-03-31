class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.end = False


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for ch in word:

            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.end = True

    def search(self, word: str) -> bool:

        curr = self.root

        for ch in word:

            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return curr.end

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for ch in prefix:

            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return True
