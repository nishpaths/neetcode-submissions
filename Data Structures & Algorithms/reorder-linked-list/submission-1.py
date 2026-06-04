# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #split the list into two
        second = slow.next
        slow.next = None

        #reverse the second list
        second_prev = None
        curr = second
        while curr:
            next = curr.next
            curr.next = second_prev
            second_prev = curr
            curr = next
        

        #now append both lists together
        p1 = head
        p2 = second_prev

        while p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1
            
            p1 = next1
            p2 = next2









