from typing import Optional, List
import heapq


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
    def merge_k_sorted_priority_queue(
        lists: List[Optional[ListNode]],
    ) -> Optional[ListNode]:
        merged = dummy = ListNode()
        heap = []

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))

        while heap:
            val, idx, node = heapq.heappop(heap)
            merged.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            merged = merged.next

        return dummy.next
