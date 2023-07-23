# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        length=0
        current = head
        while current is not None:
            current=current.next
            length+=1
        num = 0
        current = head
        power = length-1
        while current is not None:
            num+= ((2**(power))*current.val)
            power-=1
            current = current.next
        return num
