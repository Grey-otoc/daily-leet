class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next

        node = node.next

    if list1:
        node.next = list1
    else:
        node.next = list2

    return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(5)))
    
    sorted_list = mergeTwoLists(list1, list2)
    
    while sorted_list:
        print(sorted_list.val)
        sorted_list = sorted_list.next
