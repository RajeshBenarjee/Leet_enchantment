# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l=headA
        r=headB
        seti=set()
        while l is not None:
            if l not in seti:
                seti.add(l)
            l=l.next
        
        while r is not None:
            if r in seti:
                return r
            r=r.next

        return None
