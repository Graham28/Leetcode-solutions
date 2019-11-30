"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = {}
        self.log = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
          self.log.remove(key)
          self.log.append(key)
          return self.data[key]
        else:
          return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        
        if key not in self.data:
          self.data[key] = value
          if len(self.log) < self.capacity:
            self.log.append(key)
            
          else:
            del self.data[self.log[0]]
            del self.log[0]
            self.log.append(key)
        else:
          del self.data[key]
          self.log.remove(key)
          
          self.data[key] = value
          self.log.append(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)