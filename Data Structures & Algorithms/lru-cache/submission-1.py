class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Map key to node

        # Left = Least Recently Used (LRU)
        # Right = Most Recently Used (MRU)
        self.left = Node(0, 0)  # dummy LRU
        self.right = Node(0, 0) # dummy MRU
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the doubly linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert a node just before the right (MRU position)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    # Get the value of the key if it exists
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])     # move to end
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # Put a new key-value or update an existing one
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove old node

        # Add new node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Remove LRU if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
