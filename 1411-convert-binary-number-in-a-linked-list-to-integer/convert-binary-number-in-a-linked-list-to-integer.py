# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bit_number=0
        curr=head
        while curr:
            bit_number=bit_number*10+curr.val
            curr=curr.next
        
        bit_number=str(bit_number)
        # print(bit_number)
        return int(bit_number,2)