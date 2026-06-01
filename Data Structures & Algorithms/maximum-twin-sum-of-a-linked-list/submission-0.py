# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        nodes = []
        while current:
            nodes.append(current.val)
            current = current.next
        
        l,r = 0, len(nodes) - 1
        max_sum = 0
        while l < r:
            sum = nodes[l] + nodes[r]
            l = l + 1
            r = r - 1
            max_sum = max(sum, max_sum)
        return max_sum