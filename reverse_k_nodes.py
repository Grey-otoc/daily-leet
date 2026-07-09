from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    list_len = 0
    dummy = head
    while dummy:
        dummy = dummy.next
        list_len += 1
    
    prev, curr = None, head
    count = 0
    heads = []

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count += 1

        if count == k:
            heads.append(prev)
            prev = None
            count = 0
            
            if (list_len - (len(heads) * k)) < k:
                heads.append(curr)
                break

    dummy = first_head = heads[0]    
    for head in heads[1:]:
        while first_head.next:
            first_head = first_head.next
        first_head.next = head

    return dummy

if __name__ == "__main__":
    head = reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), 3)
    vals = []

    while head:
        vals.append(head.val)
        head = head.next
    
    print(vals)
