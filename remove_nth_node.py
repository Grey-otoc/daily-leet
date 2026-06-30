from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    prev, curr = None, head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    if n == 1:
        prev = prev.next  # Just skip the first node
    else:
        # Traverse to find the node BEFORE the one we want to delete
        # We need to stop at index n - 2
        dummy = prev
        count = 0
        while dummy:
            if count == n - 2 and dummy.next:
                dummy.next = dummy.next.next
                break  # Node deleted, exit loop
            count += 1
            dummy = dummy.next
    
    prev2, curr = None, prev
    
    while curr:
        temp = curr.next
        curr.next = prev2
        prev2 = curr
        curr = temp
    
    return prev2

if __name__ == "__main__":
    head = removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2)
    vals = []
    
    while head:
        vals.append(head.val)
        head = head.next

    print(vals)
