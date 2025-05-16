from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node: {self.val} -> {self.next}" if self.next else f"Node: {self.val}"


class Solution:
    @staticmethod
    def merge_sorted_linked_lists(
        list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        l1 = list1
        l2 = list2

        new_head = None
        if l1.val < l2.val:
            new_head = l1
            l1 = l1.next
        else:
            new_head = l2
            l2 = l2.next

        node = new_head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 if l1 else l2
        return new_head
