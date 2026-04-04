from typing import List


class TrieNode:

    def __init__(self) -> None:

        self.children = {}
        self.is_end_folder = False


class Solution:

    def __init__(self) -> None:

        self.root = TrieNode()

    def create(self, path: str) -> None:

        curr = self.root

        for folder in path.split("/"):

            if folder not in curr.children:
                curr.children[folder] = TrieNode()

            curr = curr.children[folder]

        curr.is_end_folder = True

    def hasParentFolder(self, path: str) -> bool:

        curr = self.root

        folders = path.split("/")

        for i in range(len(folders) - 1):

            curr = curr.children[folders[i]]

            if curr.is_end_folder:
                return True

        return False

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        for f in folder:
            self.create(f)

        res = []

        for path in folder:

            if not self.hasParentFolder(path):
                res.append(path)

        return res
