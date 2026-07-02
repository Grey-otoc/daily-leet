from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_vals = []

    curr = l1
    while curr:
        l1_vals.append(curr.val)
        curr = curr.next

    multiplier = 1
    l1_total = 0
    for val in l1_vals:
        l1_total += val * multiplier
        multiplier *= 10
        
    l2_vals = []

    curr = l2
    while curr:
        l2_vals.append(curr.val)
        curr = curr.next

    multiplier = 1
    l2_total = 0
    for val in l2_vals:
        l2_total += val * multiplier
        multiplier *= 10

    total = l1_total + l2_total
    new_head = node = ListNode(total % 10)
    total //= 10
    
    while total > 0:
        node.next = ListNode(total % 10)
        total //= 10
        node = node.next
    
    return new_head
    
if __name__ == "__main__":
    l1 = (ListNode(1, ListNode(2, ListNode(3))))
    l2 = (ListNode(4, ListNode(5, ListNode(6))))
    new_head = addTwoNumbers(l1, l2)
    
    while new_head:
        print(new_head.val)
        new_head = new_head.next
        
    print(1 % 10, 1 // 10)
