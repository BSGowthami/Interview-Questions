"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode( 0 )
        head = l
        length = 0
        #while atleast one of the linked lists is non-empty
        while l1 or l2:
            #Both linked lists are non-empty
            if l1 and l2:
                if l1.val <= l2.val:
                    l.next = ListNode( l1.val )
                    l1 = l1.next
                    l = l.next
                    continue
                else:
                    l.next = ListNode( l2.val )
                    l2 = l2.next
                    l = l.next
                    continue
            #if list 2 is empty
            if l1:
                l.next = ListNode( l1.val )
                l1 = l1.next
                l = l.next
                continue
            #if list 1 is empty
            if l2:
                l.next = ListNode( l2.val )
                l2 = l2.next
                l = l.next
                continue
        return head.next
