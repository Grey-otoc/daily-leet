from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    og_head = None
    curr = head

    while curr:
        og_head = ListNode(curr.val, curr.next)
        curr = curr.next
    
    reversed_head = None
    curr = head
    count = 0

    while curr:
        reversed_head = ListNode(curr.val, reversed_head)
        curr = curr.next
        count += 1
    
    while og_head and reversed_head and count > 0:
        if count % 2 == 0:
            head.next = og_head
            og_head = og_head.next
        else:
            head.next = reversed_head
            reversed_head = reversed_head.next
            
        head = head.next
        count -= 1
    
    head.next = None
    
    return head

if __name__ == "__main__":
    head = reorderList(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))

    while head:
        print(head.val)
        head = head.next
