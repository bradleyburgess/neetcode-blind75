from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node: {self.val} -> {self.next}" if self.next else f"Node: {self.val}"


class Solution:
    @staticmethod
    def reverse_linked_list_brute(head: Optional[ListNode]) -> ListNode:
        if not head:
            return None
        s = []

        node = head
        while node:
            s.append(node.val)
            node = node.next

        new_head = ListNode(s.pop())
        node = new_head
        while s:
            _next = ListNode(s.pop())
            node.next = _next
            node = _next

        return new_head

    @staticmethod
    def reverse_linked_list_optimized(head: Optional[ListNode]) -> ListNode:
        if not head:
            return None

        s = []
        node = head
        while node:
            s.append(node)
            node = node.next

        new_head = s.pop()
        node = new_head
        while s:
            _next = s.pop()
            node.next = _next
            node = _next

        node.next = None

        return new_head

    @staticmethod
    def reverse_linked_list_iterative(head: Optional[ListNode]) -> ListNode:
        if not head:
            return None

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
