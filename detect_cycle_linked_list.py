"""Detects if there is a cycle in a linked list"""

class LinkedList:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)

def detect_cycle(node: LinkedList) -> bool:
    slow = fast = node
    while fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

if __name__ == '__main__':
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)

    #cycle
    node1.next = node2
    node2.next = node3
    node3.next = node2
    print(detect_cycle(node1))