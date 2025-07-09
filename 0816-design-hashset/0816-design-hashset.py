class MyHashSet(object):

    def __init__(self):
        self.size = 769
        self.data = [[] for _ in range(769)]
    
    def hash(self, key):
        return key % self.size
    def add(self, key):
        i = self.hash(key)
        
        if key in self.data[i]:
            return
        else:
            self.data[i].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i=self.hash(key)
        if key in self.data[i]:
            self.data[i].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        i=self.hash(key)
        if key in self.data[i]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)