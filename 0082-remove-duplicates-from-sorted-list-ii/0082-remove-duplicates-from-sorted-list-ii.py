class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current:
            # Check if current node starts a duplicate sequence
            if current.next and current.val == current.next.val:
                # Skip all nodes with this specific duplicate value
                duplicate_val = current.val
                while current and current.val == duplicate_val:
                    current = current.next
                prev.next = current  # Link prev directly to the first non-duplicate node
            else:
                prev = current       # No duplicate, safely move prev forward
                current = current.next

        return dummy.next
