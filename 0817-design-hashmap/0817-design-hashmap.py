class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next
class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(769)]

    def hash(self, key: int) -> int:
        return key % 769
    def put(self, key: int, value: int) -> None:
        i = self.hash(key)
        # point to the dummy node of that index
        curr = self.map[i]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        i = self.hash(key)
        # point to the dummy node of that index
        curr = self.map[i]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        i = self.hash(key)
        # point to the dummy node of that index
        curr = self.map[i]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)