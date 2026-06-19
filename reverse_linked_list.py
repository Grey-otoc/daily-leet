class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev
        
if __name__ == "__main__":
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))

    new_head = reverseList(head)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
