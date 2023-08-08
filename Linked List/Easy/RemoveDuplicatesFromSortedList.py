#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        seen = set()
        current  = head
        seen.add(current.val)
        while current.next:
            if(current.next.val in seen):
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next
        return head
