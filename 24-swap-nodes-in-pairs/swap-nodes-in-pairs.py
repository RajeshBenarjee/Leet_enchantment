# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        def swap(one,two):
            temp=one.val
            one.val=two.val
            two.val=temp
        while current!=None and current.next!=None:
            swap(current,current.next)
            current=current.next.next
        return head
