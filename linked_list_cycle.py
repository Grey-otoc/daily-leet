from typing import Optional

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
        while head:
            if type(head.val) != int:
                return True
            else:
                head.val += .25
            
            head = head.next

        return False
    
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    head.next.next.next = head
    print(hasCycle(head))
