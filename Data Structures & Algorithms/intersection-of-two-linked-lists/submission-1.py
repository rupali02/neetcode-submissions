# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_len, b_len = 0, 0
        a_cur, b_cur = headA, headB

        while a_cur:
            a_len += 1
            a_cur = a_cur.next

        while b_cur:
            b_len += 1
            b_cur = b_cur.next

        if b_len > a_len:
            headA, headB = headB, headA
            a_len, b_len = b_len, a_len

        a_cur, b_cur = headA, headB

        while a_len != b_len:
            a_cur = a_cur.next
            a_len -= 1

        while b_cur:
            if a_cur == b_cur:
                return a_cur
            a_cur = a_cur.next
            b_cur = b_cur.next

        return None

        