# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


"""
### TWO-PASS NOTES ###
    1. go thru LL to get its size
    2. create dummy node that points to head
    3. decrement size and when size == n, skip next node
""" 

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        curr = head
        while curr:
            size+=1
            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr:
            if size == n:
                curr.next = curr.next.next
            else:
                curr = curr.next
            size-=1
        return dummy.next
    

"""
### ONE-PASS NOTES ###
    1. dummy node to point to head
    2. increment head n spaces
    3. while head --> move both head and curr
    4. after loop exists curr.next = curr.next.next
""" 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy

        for x in range(n):
            head = head.next

        while head:
            head = head.next
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next