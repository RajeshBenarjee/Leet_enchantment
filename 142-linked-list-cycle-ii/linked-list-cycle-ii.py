class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        # Step 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # loop ended normally -> no cycle
            return None

        # Step 2: find entry point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow