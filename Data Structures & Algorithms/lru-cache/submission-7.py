class Node: 
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.mapp = {} #holds key: Node()

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1
        node = self.mapp[key]
        self.remove(node)
        self.insertToEnd(node)

        return self.mapp[key].val

        
    def insertToEnd(self, node):
        #Insert at tail (recently used)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
            
    #whenever I call this, node is guaranteed to be in linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            node = self.mapp[key]
            self.remove(node)
            self.insertToEnd(node)
            node.val = value

        else:
            if self.size >= self.capacity:
                del self.mapp[self.head.next.key]
                self.remove(self.head.next)

            newNode = Node(key, value)
            self.insertToEnd(newNode)
            self.size += 1
            self.mapp[key] = newNode





