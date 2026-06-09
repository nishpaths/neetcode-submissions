class ListNode():
   def __init__(self, key=0, val=0):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head 

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        last = self.tail.prev
        last.next = node

        node.prev = last
        node.next = self.tail

        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        #updating
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        #adding new node
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        #removing first node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        
