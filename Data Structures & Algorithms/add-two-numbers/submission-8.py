# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        head = l1

        while l1 or l2:
            if l1 is None:
                prev.next = l2
                l1 = l2
                l2 = None
            # print(l1.val, carry, l2.val if l2 else 0)
            val_sum = l1.val + (l2.val if l2 else 0) + carry
            num = val_sum % 10
            carry = val_sum // 10
            # print("sum", num, carry, val_sum)
            l1.val = num
            prev = l1
            l1 = l1.next
            l2 = l2.next if l2 else None

        if carry:
            prev.next = ListNode(carry)

        return head




        