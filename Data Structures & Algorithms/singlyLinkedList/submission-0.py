class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        temp = self.head
        prev = None
        if temp == None:
            self.head = node
        else:
            while temp:
                prev = temp
                temp = temp.next
            prev.next = node

    def remove(self, index: int) -> bool:
        temp = self.head
        i = 0
        prev = None
        if index == 0 and temp:
            self.head = temp.next
            return True
        else:
            while temp:
                if i == index:
                    prev.next = temp.next
                    return True
                prev = temp
                temp = temp.next
                i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
