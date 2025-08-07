# 143. Reorder List
# https://leetcode.com/problems/reorder-list/


"""
### NOTES ###
"BRUTE FORCE" way
    1. loop thru LL to find its size
    2. loop thru LL again to compute an array like the LL
    3. set pointers at each end of array and update values in each node (Left & Right)
""" 

from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        size = 0
        curr = head
        while curr:
            size+=1
            curr = curr.next
        res = [0] * size
        curr = head
        idx = 0
        while curr:
            res[idx] = curr.val
            idx+=1
            curr = curr.next

        l, r = 0, len(res) - 1
        curr = head
        while l < r and curr:
            curr.val = res[l]
            curr = curr.next
            l+=1

            curr.val = res[r]
            curr = curr.next
            r-=1
        if size % 2 != 0:
            curr.val = res[l]


"""
### NOTES ###
OPTIMAL way
    1. slow and fast pointer to find middle of LL
    2. reverse 2nd half of list
    3. merge the 2 lists
    4. cry if you see this on an interview
""" 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two halfs
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2