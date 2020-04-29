"""
HashTable + linkedlist
"""

class LinkedNode:
        
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next

class LRUCache:
    
    def __init__(self, capacity: int):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        head = self.dummy.next
        
        del self.key_to_prev[head.key]
        self.key_to_prev[head.next.key] = self.dummy
        self.dummy.next = head.next
    
    def kick(self, prev): # 将数据移动到链表末尾
        node = prev.next
        if node == self.tail:
            return
        
        prev.next = node.next
        
        self.key_to_prev[node.next.key] = prev
        node.next = None
        
        self.push_back(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_prev:
            return -1
        
        prev = self.key_to_prev[key]
        current = prev.next
        self.kick(prev)
        return current.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value #NOTE
            return
        
        self.push_back(LinkedNode(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)