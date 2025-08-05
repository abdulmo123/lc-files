# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/


"""
### NOTES ###
    1. set slow and fast pointer at head
    2. move slow by one, fast by 2
    3. if slow == fast --> means you have a cylcle
""" 


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False