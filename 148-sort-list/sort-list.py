class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sorty(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            tail.next = l1 if l1 else l2
            return dummy.next

        if not head or not head.next:
            return head

        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None 
        mid = slow

        left = self.sortList(head)
        right = self.sortList(mid)
        return sorty(left, right)