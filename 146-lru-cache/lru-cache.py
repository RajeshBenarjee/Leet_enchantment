class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key=key
            self.val=val
            self.prev=None
            self.next=None

    def __init__(self, capacity: int):
        self.cap=capacity
        self.head=self.Node(-1, -1)
        self.tail=self.Node(-1, -1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cache={}

    def addNode(self, newnode):
        temp=self.head.next
        newnode.next=temp
        newnode.prev=self.head
        self.head.next=newnode
        temp.prev=newnode

    def deleteNode(self, delnode):
        prevv=delnode.prev
        nextt=delnode.next
        prevv.next=nextt
        nextt.prev=prevv

    def get(self, key: int) -> int:
        if key in self.cache:
            resNode=self.cache[key]
            ans=resNode.val
            del self.cache[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.cache[key]=self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr=self.cache[key]
            del self.cache[key]
            self.deleteNode(curr)

        if len(self.cache) == self.cap:
            del self.cache[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.cache[key]=self.head.next
