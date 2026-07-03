class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def move_node_front(self, node: Node):
        prev = self.head
        nxt = self.head.next
        node.next = nxt
        node.prev = prev
        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove_node(node)
        self.move_node_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            node.value = value
        else:
            node = Node(key, value)

        self.move_node_front(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.remove_node(lru_node)
            del self.cache[lru_node.key]

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    print(lRUCache.get(2))
    lRUCache.put(2, 6)
    print(lRUCache.get(1))
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    print(lRUCache.get(1))
    print(lRUCache.get(2))
