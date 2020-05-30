class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def prepend(self, value):
        new_head = Node(value)
        old_head = self.head
        self.head = new_head
        self.head.next = old_head

    def get(self, index):
        for i, value in enumerate(list(self)):
            if i == index:
                return value

    def insert(self, position, value):
        if position is 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            prev = None
            current = self.head

            for i in range(position):
                if current.next:
                    prev = current
                    current = current.next
                else: # `position` is out of bounds
                    return
            prev.next = new_node
            new_node.next = current

    def delete(self, position):
        if not self.head:
            return
        elif position is 0:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            for i in range(position):
                if current.next:
                    prev = current
                    current = current.next
                else:
                    return
            prev.next = current.next

    def delete_with_value(self, value):
        if self.head is None:
            return
        if self.head.value is value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def clear(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return ' '.join(map(str, list(self)))


    def has_cycle(self):
        # We have two pointers moving through the linked list at different speeds.
        # They ll eventually collide if there's a loop
        # If there's not they'll both get to the end of the linked list
        if self.head is None:
            return False
        fast = self.head.next
        slow = self.head
        while fast is not None and slow is not None and fast.next is not None:
            if fast is slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

ll = LinkedList()
ll.append(2)
ll.prepend(1)
ll.prepend(0)
ll.append(3)
ll.append(4)
assert list(ll) == list(range(5))
assert [ll.get(0), ll.get(1), ll.get(2)] == list(range(3))
assert ll.get(10) is None

ll.clear()
assert list(ll) == []
ll.insert(0,3) # 3
ll.insert(0,0) # 0 3
ll.insert(1,1) # 0 1 3
ll.insert(2,2) # 0 1 2 3
ll.insert(5,4) # out of bounds, not inserted
assert list(ll) == list(range(4))

ll.delete(0)
ll.delete(2)
ll.delete(3) # out of bounds, nothing deleted
assert list(ll) == list(range(1,3))
