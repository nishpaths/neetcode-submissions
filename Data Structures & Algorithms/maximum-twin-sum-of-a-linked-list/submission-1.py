# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find the middle:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # reverse second:
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        #find max sums
        p1 = head
        p2 = prev
        max_sum = 0
        while p1:
            max_sum = max(max_sum, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return max_sum
