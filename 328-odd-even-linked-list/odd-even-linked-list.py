# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd=ListNode()
        todd=odd
        even=ListNode()
        teven=even
        curr=head
        cnt=1
        while curr:
            if cnt&1:
                # odd index
                todd.next=ListNode(val=curr.val)
                todd=todd.next
            else:
                teven.next=ListNode(val=curr.val)
                teven=teven.next
            cnt+=1
            curr=curr.next
        # linking th last node to even list head
        todd.next=even.next
        return odd.next