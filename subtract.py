import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        if A is None:
            return A

        # calc list size and add prev pointers
        size_of_list = 0
        curr = A
        prev = None
        while (curr != None):
            size_of_list += 1
            curr.prev = prev
            prev = curr
            curr = curr.next
        tail = prev

        i = 0
        curr = A
        while (i < math.floor(size_of_list / 2)):
            curr.val = tail.val - curr.val
            curr = curr.next
            tail = tail.prev
            i += 1
        return A
