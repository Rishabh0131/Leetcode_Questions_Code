from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getLength(self, head: ListNode):
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        return n

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        listAlen = self.getLength(headA)
        listBlen = self.getLength(headB)

        currA, currB = headA, headB

        if listAlen < listBlen:
            diff = listBlen - listAlen

            while diff > 0:
                currB = currB.next  # type: ignore
                diff -= 1
        else:
            diff = listAlen - listBlen

            while diff > 0:
                currA = currA.next  # type: ignore
                diff -= 1

        while currA:
            if currA == currB:
                return currA

            currA = currA.next
            currB = currB.next  # type: ignore

        return None
