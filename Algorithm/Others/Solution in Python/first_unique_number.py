class ListNode:
    
    def __init__(self, value=None):
        self.num = value
        self.next = None
    
class FirstUnique:

    def __init__(self, nums: List[int]):
        # self.freq_dict = {}
        self.dummy = ListNode()
        self.tail = self.dummy
        self.num_to_prev = {} # 记录num对应的节点位置
        self.num_to_freq = {} # 记录num出现的freq
        
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int: # O(1)
        return self.dummy.next.num if self.dummy.next else -1

    def push_back(self, node):
        self.num_to_prev[node.num] = self.tail
        
        self.tail.next = node
        self.tail = node
        
    def remove(self, prev):
        node = prev.next
        del self.num_to_prev[node.num]
        prev.next = node.next
        
        if node != self.tail:
            self.num_to_prev[node.next.num] = prev
        else:
            self.tail = prev
        
    def add(self, value: int) -> None:
        if value not in self.num_to_freq:
            self.num_to_freq[value] = 1
            self.push_back(ListNode(value))
        elif self.num_to_freq[value] == 1:
            self.num_to_freq[value] += 1
            self.remove(self.num_to_prev[value])
        else:
            self.num_to_freq[value] += 1         
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)