# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        i = list1
        j = list2

        while i and j:
            if i.val <= j.val:
                tail.next = ListNode(i.val)
                i = i.next
            else:
                tail.next = ListNode(j.val)
                j = j.next
            tail = tail.next

        while i:
            tail.next = ListNode(i.val)
            i = i.next
            tail = tail.next

        while j:
            tail.next = ListNode(j.val)
            j = j.next
            tail = tail.next

        return dummy.next
