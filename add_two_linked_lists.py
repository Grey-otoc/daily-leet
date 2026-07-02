from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = node = ListNode()

    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        new_val = l1_val + l2_val + carry
        carry = new_val // 10
        new_val %= 10
        node.next = ListNode(new_val)

        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        node = node.next

    return dummy_head.next
    
if __name__ == "__main__":
    l1 = (ListNode(9))
    l2 = (ListNode(9))
    new_head = addTwoNumbers(l1, l2)
    
    while new_head:
        print(new_head.val)
        new_head = new_head.next
