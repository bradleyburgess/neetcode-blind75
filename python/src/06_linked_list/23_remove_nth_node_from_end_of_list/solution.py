from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node: {self.val} -> {self.next}" if self.next else f"Node: {self.val}"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


class Solution:
    @staticmethod
    def remove_from_end_two_pass(
        head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        length, node = 0, head

        while node:
            node = node.next
            length += 1

        if n == length:
            return head.next

        node_index = length - n
        current = 0
        node = head
        while current < node_index - 1:
            current += 1
            node = node.next

        node.next = node.next.next
        return head

    def remove_from_end_floyd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast, fast_idx = head, 0

        while fast and fast_idx < n:
            fast = fast.next
            fast_idx += 1

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            # fast_idx +=1
            slow = slow.next

        slow.next = slow.next.next

        return head

    def remove_from_end_floyd_dummy(
        head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        dummy = slow = fast = ListNode(0, head)
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
