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