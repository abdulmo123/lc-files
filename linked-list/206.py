# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/


"""
### NOTES ###
    1. set up a prev null node
    2. set a curr at the head
    2. at each step: 
        a. set the next to curr's next
        b. set curr's next to prev
        c. set prev to curr
        d. set curr to the next
""" 


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev