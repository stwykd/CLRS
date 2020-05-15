class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data is data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

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
