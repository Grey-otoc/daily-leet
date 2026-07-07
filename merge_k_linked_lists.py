from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i+1] if (i + 1) < len(lists) else None
            mergedList = mergeList(list1, list2)
            mergedLists.append(mergedList)

        lists = mergedLists

    return lists[0]

def mergeList(list1: list[ListNode], list2: list[ListNode]) -> ListNode:
    head = tail = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    tail.next = list1 if list1 else list2

    return head.next
    
if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(5)))
    list3 = ListNode(3, ListNode(6))
    lists = [list1, list2, list3]
    
    head = mergeKLists(lists)
    
    while head:
        print(head.val)
        head = head.next
