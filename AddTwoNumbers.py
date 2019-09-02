# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import math


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(None)
        cookie = l3

        carryover = 0

        while (True):
            totalv = l1.val + l2.val + carryover
            currDig = totalv % 10
            carryover = int(math.floor(totalv / 10))
            # print(str(l1) + ", " + str(l2)+": " + str(currDig) + ", " + str(carryover))
            l3.val = currDig

            if l1.next == None and l2.next == None:
                break;

            l3.next = ListNode(0)
            l3 = l3.next

            if l1.next == None:
                l1.next = ListNode(0)
                l1.next.val = 0
            if l2.next == None:
                l2.next = ListNode(0)
                l2.next.val = 0

            l1 = l1.next
            l2 = l2.next

        if carryover > 0:
            l3.next = ListNode(carryover)

        return cookie