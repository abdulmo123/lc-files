# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


"""
### NOTES ###
    1. set up an empty node (ex: -1)
    2. set a list 3 pointer that starts at that empty node
    3. iterate thru list1 and list2 at the same time
    4. at each step: 
        a. if list1.val > list2.val --> 
            - set list 3 pointer to list2's val 
            - increment list2 to its next pointer
        b. else if list1.val < list2.val --> 
            - set list 3 pointer to list1's val
            - incrememnt list1 to its next pointer
    5. if by the end, one of the lists isn't finished, just append its items to the end of list3
""" 

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(-1)
        l3 = list3

        while list1 and list2:
            if list1.val > list2.val:
                l3.next = list2
                list2 = list2.next
            else:
                l3.next = list1
                list1 = list1.next
            l3 = l3.next
        
        if list1:
            l3.next = list1
        if list2:
            l3.next = list2
        
        return list3.next